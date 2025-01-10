import argparse
import re
from time import mktime
from pprint import pprint
from pygooglenews import GoogleNews
from tqdm import tqdm

from google_news_url_decoder import get_decoded_url
from newspaper3k_scraper import get_article_data


def search_google(query: str, time_delta: str):
    """
    Searches Google News for the given query within a specified time range.

    Args:
        query (str): The search term to query Google News.
        time_delta (str): The time range for the search, e.g., '30d' for 30 days, '15h' for 15 hours.

    Yields:
        dict: A dictionary containing the news title, summary, link, publication date, and article data.
    """
    # Initialize GoogleNews object
    gn = GoogleNews()

    # Perform the search
    news = gn.search(query=query, when=time_delta)

    # Sort news entries by publication time in descending order
    sorted_news = sorted(news["entries"], key=lambda x: mktime(x['published_parsed']), reverse=True)

    # Process each news entry
    for entry in sorted_news:
        # Extract and store key details for each news item
        news_item = {
            "title": entry["title"],
            "summary": entry["summary"],
            "link": entry["link"],
            "published": entry["published"]
        }

        # Extract main content from the summary using regex
        match = re.search(r'<a [^>]*>(.*?)</a>', entry["summary"])
        if match:
            # Replace summary with the extracted content
            news_item["summary"] = match.group(1)

        # Extract decoded URL from Google News redirect URL
        decoded_url = get_decoded_url(entry["link"])
        if decoded_url:
            news_item["link"] = decoded_url

        # Yield the processed news item as it's ready
        yield news_item


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search for a company with a specified time range.")

    # Add arguments for query and time_delta with flags
    parser.add_argument('--query', type=str, required=True, help="Search query (e.g., company name).")
    parser.add_argument('--time_delta', type=str, required=True,
                        help="Time range for the search (e.g., '30d', '15h', '20s').")

    # Parse the arguments
    args = parser.parse_args()

    # Perform the search and store results in a generator
    news_generator = search_google(query=args.query, time_delta=args.time_delta)

    # Count total news items for progress bar initialization
    gn = GoogleNews()
    total_items = len(gn.search(query=args.query, when=args.time_delta)["entries"])

    # Set up the progress bar
    with tqdm(total=total_items, desc="Processing News", unit="item") as pbar:
        for news_item in news_generator:
            # Print the news item as it's processed
            pprint(news_item)
            # Extract article data and add it to the news item
            article_data = get_article_data(url=news_item["link"])
            pprint(article_data)
            news_item["article"] = article_data
            # Update the progress bar
            pbar.update(1)
