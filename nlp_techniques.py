import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from textblob import TextBlob
from nltk.corpus import stopwords

# Initialize spaCy model for NER (Named Entity Recognition)
nlp = spacy.load("en_core_web_sm")

# import nltk
# nltk.download('stopwords')

def refine_summary(article_text, sentence_count=3):
    """
    Refines the summary of the article using LexRank (sumy) for better relevance.
    """
    parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
    summarizer_lexrank = LexRankSummarizer()
    refined_summary = summarizer_lexrank(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in refined_summary)


def analyze_sentiment(article):
    """
    Analyzes sentiment of both the main text and the summary.
    """
    sentiment_main_text = get_sentiment_score(article.text)
    sentiment_summary = get_sentiment_score(article.summary)
    return {
        "main_text_sentiment": sentiment_main_text,
        "summary_sentiment": sentiment_summary
    }


def get_sentiment_score(text):
    """
    Analyzes the sentiment of a text using TextBlob.
    """
    sentiment = TextBlob(text).sentiment
    return {"polarity": sentiment.polarity, "subjectivity": sentiment.subjectivity}


def enrich_keywords(article):
    """
    Enhances the keyword list by removing common stop words.
    """
    stop_words = set(stopwords.words('english'))
    enriched_keywords = [kw for kw in article.keywords if kw.lower() not in stop_words]
    return enriched_keywords


def extract_named_entities(text):
    """
    Extracts named entities using spaCy.
    """
    doc = nlp(text)
    entities = {ent.text for ent in doc.ents}
    return entities
