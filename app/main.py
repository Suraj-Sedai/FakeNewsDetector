from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, root_validator
from typing import Optional
from .data_queue import ArticleQueue, SeenURLs, HistoryStack
from .lru_cache import LRUCache
from .summarizer import summarize
from .article_scraper import extract_text_from_url
from .classifier import classify

app = FastAPI()

# Global instances
article = ArticleQueue()
urls = SeenURLs()
cache = LRUCache(capacity=100)  # global LRU cache
history = HistoryStack()

# Request model
class ProcessRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

    @root_validator(pre=True)
    def at_least_one_field_required(cls, values):
        if not values.get("text") and not values.get("url"):
            raise ValueError("At least one of 'text' or 'url' must be provided.")
        return values

#Create an /undo Endpoint
@app.post("/undo")
def undo_last():
    if history.is_empty():
        raise HTTPException(status_code=400, detail="No article to undo.")
    
    undone = history.pop()
    return {"status": "undone", "undone_article": undone}
    
# /process endpoint
@app.post("/process")
async def process_data(request: ProcessRequest):
    key = request.url or request.text  # unified cache key

    # ✅ Check cache
    cached = cache.get(key)
    if cached:
        return {"status": "cached", **cached}

    # ✅ Check for seen URL
    if request.url:
        if urls.has_seen(request.url):
            raise HTTPException(status_code=400, detail="This URL has already been processed.")
        urls.add_url(request.url)
        article.enqueue(request.url)

    # If URL was given but no text, extract article text
    if request.url and not request.text:
        try:
            extracted_text = extract_text_from_url(request.url)
        except Exception:
            raise HTTPException(status_code=400, detail="Failed to extract article from URL.")
    else:
        extracted_text = request.text


    # ✅ Dummy processing result
    result = {
        "source": "url" if request.url else "text",
        "summary": summarize(extracted_text),
        **classify(extracted_text)
    }

    history.push(result)

    # ✅ Store result in LRU cache
    cache.put(key, result)

    return {"status": "success", **result}
