"""Tools to train a language classification model

This modules contains functions to extract multi-lingual text documents from
Wikipedia articles to be able to train a machine learning model to classify the
language of a piece of text.
"""
from pathlib import Path

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

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


def build_language_detector(texts, labels, random_state=None):
    language_detector = make_pipeline(
        TfidfVectorizer(analyzer="char", ngram_range=(1, 3),
                        min_df=2, max_df=0.9, norm="l2", dtype=np.float32),
        SGDClassifier(early_stopping=True, validation_fraction=0.2,
                      n_iter_no_change=3, max_iter=1000, tol=1e-3,
                      alpha=1e-5, penalty="l2",
                      random_state=random_state)
    )
    return language_detector.fit(texts, labels)
