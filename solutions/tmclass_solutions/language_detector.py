"""Tools to train a language classification model

This modules contains functions to extract multi-lingual text documents from
Wikipedia articles to be able to train a machine learning model to classify the
language of a piece of text.

"""
from pathlib import Path
from tmclass_solutions.scraping import WikipediaArticle


def wikipedia_language(filepath):
    for part in Path(filepath).parts:
        if part.endswith(".wikipedia.org"):
            return part.split(".")[0]
    raise ValueError(f"{str(filepath)} has no Wikipedia language information")


def split_paragraphs(text, min_length=30):
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if len(p.strip()) >= min_length]


def make_language_detector_dataset(html_filepaths, min_length=30):
    texts, language_labels, article_names = [], [], []
    for html_filepath in html_filepaths:
        language_label = wikipedia_language(html_filepath)
        article_name = html_filepath.parent.name
        article = WikipediaArticle(html_filepath.read_bytes(),
                                   encoding="utf-8")
        text = article.get_main_text()
        for short_text in split_paragraphs(text, min_length):
            texts.append(short_text)
            language_labels.append(language_label)
            article_names.append(article_name)
    return texts, language_labels, article_names
