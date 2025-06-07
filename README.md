# 🧠 Fake News Detector & Summarizer

A real-time news analysis system built from scratch using Python and FastAPI.  
It summarizes news articles using the T5 model and detects fake or real news using a fine-tuned BERT classifier.  
The system is powered by core data structures like Queue, Stack, HashMap, and a custom LRU Cache for performance and reliability.

## ✅ Features

- Summarize long news articles using the T5 model.
- Classify news articles as FAKE or REAL using BERT.
- Cache previously processed articles using an LRU Cache.
- Skip duplicate URLs using a HashMap (set).
- Support rollback using a Stack for the last processed articles.
- Simulate real-time streaming using a Queue.
- Full CLI support for terminal interaction.
- Clean, modular FastAPI backend.

## 🗂️ Folder Structure

```
FakeNewsDetector/
├── app/
│   ├── main.py           # FastAPI backend entry
│   ├── summarizer.py     # T5 summarizer logic
│   ├── classifier.py     # BERT fake news classifier
│   ├── lru_cache.py      # LRU cache (DLL + HashMap)
│   ├── data_queue.py     # Queue and Stack implementations
│   └── utils.py          # Utility functions
├── models/               # Pretrained or saved models
├── cli.py                # CLI entry point
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

### ➤ Queue
Simulates incoming articles in a streaming environment.  
Implements FIFO logic to ensure chronological processing.

### ➤ HashMap (Set)
Tracks previously seen URLs.  
Skips repeated URLs to avoid reprocessing.

### ➤ Stack
Stores last N processed articles.  
Used to roll back or undo the last action.

### ➤ LRU Cache
Custom implementation using Doubly Linked List + HashMap.  
Caches summary and classification results for quick reuse.

### ➤ Summarization
Uses the T5 transformer model (`t5-small`) to generate short summaries from full news text.

### ➤ Classification
Uses BERT (`bert-base-uncased`) model fine-tuned on a fake news dataset to classify articles.

## 🔌 API Design

### POST `/process`

#### Input (Choose one):
```json
{ "url": "https://example.com/article" }
```
OR
```json
{ "text": "Breaking news just in..." }
```

#### Output:
```json
{
  "summary": "The economy is improving...",
  "classification": {
    "label": "real",
    "confidence": 0.92
  },
  "cached": false,
  "message": "Processed successfully"
}
```

## 💻 CLI Usage

```bash
# Process using a URL
python cli.py --url "https://example.com/article"

# Process using raw text
python cli.py --text "Some news headline or paragraph..."

# Undo last processed article
python cli.py --undo
```

## 🧪 Datasets Used

- **LIAR Dataset**  
  Political statements labeled with truth/fake labels.  
  📎 https://www.cs.ucsb.edu/~william/data/liar_dataset.zip

- **FakeNewsNet**  
  Labeled dataset with full news articles.  
  📎 https://github.com/KaiDMML/FakeNewsNet

## 🧰 Installation & Run

### 1. Clone & Set Up Environment

```bash
git clone https://github.com/Suraj-Sedai/FakeNewsDetector
cd FakeNewsDetector
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Backend Server

```bash
uvicorn app.main:app --reload
# Visit the API docs at:
# http://127.0.0.1:8000/docs
```

### 4. Use CLI

```bash
python cli.py --url "https://example.com/article"
```

## 📤 Example Output

### From CLI:

```bash
$ python cli.py --text "Breaking news: The moon landing was faked..."
Summary: There are conspiracies regarding the moon landing...
Classification: FAKE (0.94)
```

### Undo Example:

```bash
$ python cli.py --undo
Undoing last article...
```

## 🧠 Data Structures Breakdown

| Feature             | Data Structure         | Purpose                               |
|---------------------|------------------------|----------------------------------------|
| Streaming Queue     | Queue (`deque`)        | Handle incoming articles in order     |
| Undo                | Stack (`list`)         | Rollback last processed article       |
| URL Deduplication   | HashSet (`set`)        | Skip previously processed articles    |
| Smart Cache         | LRU (DLL + HashMap)    | Store recent summary/classify results |

## 🧾 requirements.txt

```
fastapi
uvicorn
transformers
torch
newspaper3k
beautifulsoup4
```

## 💡 Extra Features (Planned)

- [ ] React frontend dashboard
- [ ] Sentiment analysis of headlines
- [ ] Trending topic extraction
- [ ] Browser extension for live verification

## 👤 Author

Built with ❤️ by [Suraj Sedai](https://github.com/Suraj-Sedai)  
An international CS student exploring AI + data structures through hands-on projects.

## 🪪 License

This project is licensed under the **MIT License**.  
Free to use, modify, and share for academic and personal purposes.

## 🔗 GitHub

[🔗 FakeNewsDetector Repository](https://github.com/Suraj-Sedai/FakeNewsDetector)