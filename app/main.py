from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, root_validator
from typing import Optional
from data_queue import ArticleQueue, SeenURLs
from lru_cache import LRUCache

app = FastAPI()

# Global instances
article = ArticleQueue()
urls = SeenURLs()
cache = LRUCache(capacity=100)  # global LRU cache

# Request model
class ProcessRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

    @root_validator(pre=True)
    def at_least_one_field_required(cls, values):
        if not values.get("text") and not values.get("url"):
            raise ValueError("At least one of 'text' or 'url' must be provided.")
        return values

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

    # ✅ Dummy processing result
    result = {
        "source": "url" if request.url else "text",
        "summary": "This is a dummy summary.",
        "confidence": 0.95,
        "label": "real"
    }

    # ✅ Store result in LRU cache
    cache.put(key, result)

    return {"status": "success", **result}
