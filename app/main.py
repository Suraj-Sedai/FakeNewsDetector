from fastapi import FastAPI
from pydantic import BaseModel, root_validator
from typing import Optional
from data_queue import ArticleQueue, SeenURLs

app = FastAPI()
article = ArticleQueue(app)
urls = SeenURLs(app)
class ProcessRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None
    # If a URL is given, check if it's already in seen_urls
    # If yes → return response like "Already processed"
    if url in urls.seen_urls:
        raise ValueError("This URL has already been processed.")
    
    # If not → add to seen_urls, and enqueue the article
    else:
        urls.add_url(url)
        article.enqueue(url)

    @root_validator(pre=True)
    def at_least_one_field_required(cls, values):
        if not values.get("text") and not values.get("url"):
            raise ValueError("At least one of 'text' or 'url' must be provided.")
        return values

@app.post("/process")
async def process_data(request: ProcessRequest):
    dummy_response = {
        "status": "success",
        "source": "text" if request.text else "url",
        "summary": "This is a dummy summary.",
        "confidence": 0.95,
        "label": "real"
    }
    return dummy_response
