from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text:str) -> str:
    output = summarizer(text, max_length= 130, min_length = 30, do_sample=False)
    summary_text = output[0]["summary_text"]
    return summary_text