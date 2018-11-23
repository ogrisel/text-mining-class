"""Tools to train a language classification model

This modules contains functions to extract multi-lingual text documents from
Wikipedia articles to be able to train a machine learning model to classify the
language of a piece of text.
"""
from pathlib import Path

import numpy as np
from gzip import GzipFile
import pickle

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

from tmclass_solutions.scraping import WikipediaArticle
from tmclass_solutions import MODEL_FOLDER_PATH


LANGUAGE_CLASSIFIER_PATH = MODEL_FOLDER_PATH / "language_classifier.pkl.gz"


def wikipedia_language(filepath):
    """Parse the filename to find the language code of a scraped wikipedia file

    The function assumes a path such as:

        /some/folder/xyz.wikipedia.org/some/file

    This function returns the language code xyz (2 or 3 letters).

    Raise `ValueError` if filepath has no wikipedia hostname component.
    """
    for part in Path(filepath).parts:
        if part.endswith(".wikipedia.org"):
            return part.split(".")[0]
    raise ValueError(f"{filepath} has no Wikipedia language information")


def split_paragraphs(text, min_length=30):
    """Extract a list of paragraphs from text

    Return a list of strings. Paragraphs are separated by double "new-line"
    characters.

    Any paragraph shorter than min_length is dropped.

    Any whitespaces at the beginning or ending of paragraphs are trimmed.
    """
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


def build_language_classifier(texts, labels, verbose=False, random_state=None):
    language_classifier = make_pipeline(
        TfidfVectorizer(analyzer="char", ngram_range=(1, 3),
                        min_df=2, max_df=0.9, norm="l2", dtype=np.float32),
        SGDClassifier(early_stopping=True, validation_fraction=0.2,
                      n_iter_no_change=3, max_iter=1000, tol=1e-3,
                      alpha=1e-5, penalty="l2", verbose=verbose,
                      random_state=random_state)
    )
    return language_classifier.fit(texts, labels)


class LanguageDetector:
    """Helper tool to use a pretrained mode to detect language from text"""

    def __init__(self, model):
        if isinstance(model, Path):
            opener = GzipFile if model.name.endswith(".gz") else open
            with opener(model, 'rb') as f:
                model = pickle.load(f)
        self.model = model

    def __call__(self, text):
        if text == "":
            # Do not trust the bias of the model for such an extreme case.
            return None
        return self.model.predict([text])[0]


def get_language_detector():
    """"Load a language detector from a pre-trained model"""
    if LANGUAGE_CLASSIFIER_PATH.exists():
        return LanguageDetector(LANGUAGE_CLASSIFIER_PATH)
    else:
        return None
