"""Tools to train a language classification model

This modules contains functions to extract multi-lingual text documents from
Wikipedia articles to be able to train a machine learning model to classify the
language of a piece of text.
"""
from pathlib import Path

# import numpy as np
from gzip import GzipFile
import pickle

# from sklearn.pipeline import make_pipeline
# from sklearn.linear_model import SGDClassifier
# from sklearn.feature_extraction.text import TfidfVectorizer

# from tmclass_solutions.scraping import WikipediaArticle
from tmclass_solutions import MODEL_FOLDER_PATH


LANGUAGE_CLASSIFIER_PATH = MODEL_FOLDER_PATH / "language_classifier.pkl.gz"


def wikipedia_language(filepath):
    """Parse the filename to find the language code of a scraped wikipedia file

    The function assumes a path such as:

        /some/folder/xyz.wikipedia.org/some/file

    This function returns the language code xyz (2 or 3 letters).

    Raise `ValueError` if filepath has no wikipedia hostname component.
    """
    # Hints:
    # - `Path(filepath).parts` returns the list of string components of a path.
    # - Use `my_string.startswith(prefix)` or `my_string.endswith(suffix)``
    #   to detect if `my_string` has a specific string prefix or suffix.
    # - Use `my_string.split(separator)` to split a string.
    # - Use `raise ValueError("Some informative message") if the input value
    #   is not valid.

    # TODO: change the following:
    return "en"


def split_paragraphs(text, min_length=30):
    """Extract a list of paragraphs from text

    Return a list of strings. Paragraphs are separated by double "new-line"
    characters.

    Any paragraph shorter than min_length is dropped.

    Any whitespaces at the beginning or ending of paragraphs are trimmed.
    """
    # Hints:
    # - The new line character is "\n". Some Windows applications also use
    #   "\r\n" but this convention not used by our wikipedia scraper.

    # TODO: change the following:
    return [text]


def make_language_detector_dataset(html_filepaths, min_length=30):
    """Turn scraped wikipedia articles into a language dection dataset

    This function extracts all the paragraphs from the HTML pages scraped from
    Wikipedia and filters out paragraph that are shorted than min_length.

    For each paragraph, the language and the article name of the paragraph are
    also collected in auxilary lists.

    This functions returns the list of texts in paragraph, the list of language
    codes, and the list of article names. The three lists have the same number
    of elements (with repeated values for the language and article names
    lists).
    """
    # Hints:
    # - Reuse previously implemented functions and classes when appropriate.
    # - To retrieve the the name of the parent folder of a filepath, use
    #   filepath.parent.name
    # - Use the `.append()` method to add elements to each of the three lists
    #   in the same loops so as to make sure that the three lists have matching
    #   lengths.
    texts, language_labels, article_names = [], [], []
    # TODO: implement me!
    return texts, language_labels, article_names


def build_language_classifier(texts, labels, random_state=None):
    """Train a text classifier with scikit-learn

    The text classifier is composed of two elements assembled in a pipeline:

    - A text feature extractor (`TfidfVectorizer`) that extract the relative
      frequencies of unigrams, bigrams and trigrams of characters in the text.

    - An instance of `SGDClassifier` for the classification it-self. To speed
      up training it is recommended to enable early stopping.

    `random_state` is passed to the underlying `SGDClassifier` instance.
    """
    # Hints:
    # - Look for examples of text classification pipelines in the scikit-learn
    #   documentation: https://scikit-learn.org
    # - Pass `analyzer="char"` to `TfidfVectorizer` to use character-level
    #   features instead of word-level features.
    # - Call the `fit` of the pipeline to train the model with `texts` as the
    #   input data and `labels` as target variable.
    # - You might want to use a jupyter notebook to interactively try many
    #   model parameters and use cross-validation to find which parameter give
    #   good results and a fast training time.

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
