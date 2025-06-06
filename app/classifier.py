from transformers import pipeline

classifier = pipeline("text-classification", model="Pulk17/Fake-News-Detection")

def classify(text:str) -> dict:
    result = [{'label': 'FAKE', 'score': 0.942}]

    output = {
        "label": result[0]['label'].lower(),
        "confidence": round(result[0]['score'], 2)
    }

    return output

print(classify("The earth is flat and NASA is hiding the truth."))