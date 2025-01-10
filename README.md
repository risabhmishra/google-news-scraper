# 📰 Google News Scraper

**Google News Scraper** is a Python-based project designed to fetch and process Google News articles effortlessly. Whether you're conducting research, tracking the latest news, or performing sentiment analysis, this tool empowers you to extract and analyze news data with ease. 

## 🚀 Features
- **Customizable News Search**: Fetch articles based on your search query and time range.
- **Automatic URL Decoding**: Decodes Google News redirect URLs to obtain actual article links.
- **Article Extraction**: Extracts clean text content from the fetched articles.
- **NLP Integration**: Performs basic Natural Language Processing (NLP) on the extracted data (customizable).
- **Progress Tracking**: Displays a progress bar with `tqdm` for scraping and processing articles.

## 📦 Installation
To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/risabhmishra/google-news-scraper.git
cd google-news-scraper
pip3 install -r requirements.txt
```

## 💻 Usage
Run the scraper with a simple command:

```bash
python3 google_news_scraper.py --query "Query Params" --time_delta "Time Delta"
```

### Arguments
- `--query`: Search term(s) for Google News (e.g., "AI technology").
- `--time_delta`: Filter articles by age (e.g., `24h` for 24 hours, `7d` for 7 days, or `120s` for 120 seconds).

## 🔍 How It Works
1. **Fetch News Links**: Searches Google News for articles matching your query.
2. **Decode URLs**: Decodes Google News redirect links to get the original article URLs.
3. **Extract Articles**: Downloads and extracts clean text content from each article.
4. **Perform NLP**: Applies basic NLP operations (customizable for advanced needs).
5. **Track Progress**: Visualizes scraping and processing progress using a sleek progress bar.

## 📖 Example
Search for news about "ceinsys tech ltd" from the past 15 days:

```bash
python3 google_news_scraper.py --query "ceinsys tech ltd" --time_delta "15d"
```

## 🛠️ Customization
Easily extend functionality:
- **Advanced NLP**: Add sentiment analysis, keyword extraction, or summarization.
- **Data Storage**: Save results in formats like JSON, CSV, or a database.
- **Automation**: Schedule periodic scraping tasks with cron jobs or task schedulers.

## 🎨 Progress Visualization
Enjoy a smooth user experience with a detailed progress bar powered by `tqdm`:
```bash
[####                  ] 25% Decoding URLs
```

## 📋 Output Example
```json
[
  {
    "title": "Ceinsys Tech achieves breakthrough in geospatial technology",
    "url": "https://example.com/ceinsys-tech",
    "content": "Ceinsys Tech Ltd has revolutionized geospatial solutions...",
    "timestamp": "2024-01-01"
  },
  ...
]
```

## 🤝 Contributing
We welcome contributions to enhance this project! Check out our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🌟 Why Use This Tool?
- No need to manually search for and decode Google News links.
- Lightweight and customizable for a wide range of use cases.
- Perfect for news aggregation, research, and analytics.

## 📜 License
This project is licensed under the [MIT License](LICENSE).
