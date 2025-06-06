from transformers import pipeline

classifier = pipeline("text-classification", model="mrm8488/bert-tiny-fake-news")

def classify(text:str) -> dict:
    result = classifier(text)

    label = result[0]['label']
    score = round(result[0]['score'], 2)

    
    return result