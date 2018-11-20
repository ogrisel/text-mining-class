"""Tools to train a language classification model

This modules contains functions to extract multi-lingual text documents from
Wikipedia articles to be able to train a machine learning model to classify the
language of a piece of text.
"""
from pathlib import Path

from gzip import GzipFile
import pickle

from tmclass_solutions import MODEL_FOLDER_PATH


LANGUAGE_CLASSIFIER_PATH = MODEL_FOLDER_PATH / "language_classifier.pkl.gz"


def wikipedia_language(filepath):
    # TODO: change the following:
    return "en"


def split_paragraphs(text, min_length=30):
    # TODO: change the following:
    return [text]


def make_language_detector_dataset(html_filepaths, min_length=30):
    texts, language_labels, article_names = [], [], []
    # TODO: implement me!
    return texts, language_labels, article_names


def build_language_classifier(texts, labels, random_state=None):
    # TODO: implement me!
    return None


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
