import logging
from pprint import pprint

from newspaper import Article

from nlp_techniques import enrich_keywords, refine_summary, analyze_sentiment, extract_named_entities

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Log to console
    ]
)

def get_article_data(url: str) -> dict:
    """
    Extracts structured data from an article given its URL.

    Args:
        url (str): The URL of the article to scrape.

    Returns:
        dict: A dictionary containing extracted article data including headline, authors,
              publication date, main text, top image, keywords, and summary.

    Raises:
        ValueError: If the URL is invalid or if article download/parsing fails.
    """
    if not url or not isinstance(url, str):
        logging.error("Invalid URL provided.")
        raise ValueError("The provided URL is not valid.")

    logging.info(f"Processing URL: {url}")

    # Initialize the Article object
    article = Article(url)

    try:
        # Download the article content
        article.download()
        article.parse()
    except Exception as e:
        logging.error(f"Error downloading or parsing the article: {e}")
        raise ValueError(f"Unable to process the article at {url}: {e}")

    try:
        # Perform NLP operations
        article.nlp()
    except Exception as e:
        logging.warning(f"NLP processing failed for the article: {e}")
        # Proceed without keywords/summary if NLP fails

    # Extract desired data
    data = {
        "headline": article.title or "N/A",
        "authors": article.authors or [],
        "publication_date": article.publish_date or "N/A",
        "main_text": article.text or "",
        "top_image": article.top_image or "N/A",
        "keywords": enrich_keywords(article),
        "summary": refine_summary(article.text),
        "sentiment": analyze_sentiment(article),
        "named_entities": extract_named_entities(article.text)
    }

    logging.info(f"Successfully extracted data from: {url}")
    return data


if __name__ == '__main__':
    # Example article URL
    url = "https://www.nbmcw.com/news/ceinsys-tech-wins-rs385-cr-bid-for-wainganga-nalganga-river-link-project.html#:~:text=The%20%E2%82%B9385.15%20crore%20contract,preparing%20the%20project's%20detailed%20report"

    try:
        # Fetch article data
        article_data = get_article_data(url=url)
        pprint(article_data)
    except ValueError as e:
        logging.error(f"Failed to process article: {e}")
