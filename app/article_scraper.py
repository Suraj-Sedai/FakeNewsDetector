from newspaper import Article

def extract_text_from_url(url: str) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print("❌ ERROR while extracting article:", e)
        raise RuntimeError("Failed to extract article from URL.") from e
