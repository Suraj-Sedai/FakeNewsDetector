import argparse
from app.summarizer import summarize
from app.article_scraper import extract_text_from_url
from app.classifier import classify


def get_cli_args():
    parser = argparse.ArgumentParser(
        description="🧠 Fake News Detector & Summarizer CLI 🔍"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--text", type=str, help="Direct input text for analysis"
    )
    group.add_argument(
        "--url", type=str, help="URL of an article to fetch and analyze"
    )

    return parser.parse_args()


def main():
    args = get_cli_args()

    # Step 1: Get content
    if args.text:
        content = args.text
    else:
        try:
            content = extract_text_from_url(args.url)
        except Exception as e:
            print(f"❌ Error fetching article from URL: {e}")
            return

    # Step 2: Summarize content
    print("\n✅ Summary:")
    summary = summarize(content)
    print(f"   {summary.strip()}")

    # Step 3: Classify summary
    print("\n🔍 Classification:")
    result = classify(summary)
    print(f"   Label: {result['label']}")
    print(f"   Confidence: {result['confidence']:.2f}")


if __name__ == "__main__":
    main()
