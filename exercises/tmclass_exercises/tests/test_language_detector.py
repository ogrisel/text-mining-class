from collections import Counter
import json
import pytest
from numpy.testing import assert_array_equal
import pandas as pd
from sklearn.model_selection import train_test_split

from tmclass_exercises.language_detector import wikipedia_language
from tmclass_exercises.language_detector import split_paragraphs
from tmclass_exercises.language_detector import make_language_detector_dataset
from tmclass_exercises.language_detector import build_language_classifier
from tmclass_exercises.language_detector import get_language_detector
from tmclass_exercises.data_download import download_wikipedia_scraping_result
from tmclass_exercises.data_download import download_wikipedia_language_dataset
from tmclass_exercises import DATA_FOLDER_PATH


def test_wikipedia_language():
    assert wikipedia_language("/path/to/it.wikipedia.org/wiki/Roma") == "it"
    assert wikipedia_language("azb.wikipedia.org") == "azb"
    assert wikipedia_language("fr.wikipedia.org/wiki/Portail:Accueil") == "fr"

    with pytest.raises(ValueError) as excinfo:
        wikipedia_language("/home/ogrisel")

    expected_message = "/home/ogrisel has no Wikipedia language information"
    assert str(excinfo.value) == expected_message


MULTI_PARAGRAPH_DOCUMENT = """\

This is the first paragraph. Is it not very interesting but it is the first
paragraph in the document.

And here is the second paragraph. It is much more interesting. This is the
second paragraph. This paragraph is very repetitive. This paragraph is very
repetitive. This paragraph is very repetitive. This paragraph is very
repetitive.

To short a paragraph.

This the third valid paragraph. It's boring but at least it's the final
paragraph.

"""

SHORT_DOCUMENT = "This is a very short document. It has only one line."


def test_split_paragraph_30():
    paragraphs = split_paragraphs(SHORT_DOCUMENT, min_length=30)
    assert len(paragraphs) == 1
    assert paragraphs[0] == SHORT_DOCUMENT

    paragraphs = split_paragraphs(MULTI_PARAGRAPH_DOCUMENT, min_length=30)
    assert len(paragraphs) == 3
    assert paragraphs[0].startswith("This is the first paragraph.")
    assert paragraphs[0].endswith("first\nparagraph in the document.")
    assert paragraphs[1].startswith("And here is the second paragraph.")
    assert paragraphs[1].endswith("very\nrepetitive.")
    assert paragraphs[2].startswith("This the third valid paragraph.")
    assert paragraphs[2].endswith("final\nparagraph.")
    assert all(len(p) > 30 for p in paragraphs)


def test_split_paragraph_100():
    paragraphs = split_paragraphs(SHORT_DOCUMENT, min_length=100)
    assert len(paragraphs) == 0
    paragraphs = split_paragraphs(MULTI_PARAGRAPH_DOCUMENT, min_length=100)
    assert len(paragraphs) == 2
    assert paragraphs[0].startswith("This is the first paragraph.")
    assert paragraphs[0].endswith("first\nparagraph in the document.")
    assert paragraphs[1].startswith("And here is the second paragraph.")
    assert paragraphs[1].endswith("very\nrepetitive.")


def test_language_detector_dataset():
    # Make sure that the pre-scraped dataset is available
    download_wikipedia_scraping_result()

    scraping_folder = DATA_FOLDER_PATH / "wikipedia_scraping"
    html_filepaths = sorted(scraping_folder.glob("**/body"))

    texts, language_labels, article_names = make_language_detector_dataset(
        html_filepaths, min_length=30)

    assert len(texts) == len(language_labels) == len(article_names)
    assert len(texts) >= 10000

    text_lengths = [len(text) for text in texts]
    assert min(text_lengths) >= 30
    assert max(text_lengths) <= 10000

    assert article_names[0] == "أدب"
    assert language_labels[0] == "ar"

    assert article_names[-1] == "音乐"
    assert language_labels[-1] == "zh"

    # Check that our 29 different languages are represented
    label_counts = Counter(language_labels)
    assert len(label_counts) == 29

    # Check that all the classes are well represented and none is overly
    # represented.
    for label, count in label_counts.items():
        assert count >= 100, label
        assert count <= 1500, label

    label, count = label_counts.most_common(n=1)[0]
    assert label == "fr"
    assert count >= 1000

    # Convert the resulting python lists to the columns of a pandas dataframe
    # so as to save the resulting dataset as a parquet file which is a very
    # efficient and fast way to store heterogeneously typed tabulare data
    # sets.

    # dataset = pd.DataFrame({
    #     "article_name": article_names,
    #     "language": language_labels,
    #     "text": texts,
    # })
    # dataset.to_parquet(DATA_FOLDER_PATH / "wikipedia_language.parquet")


def test_build_language_classifier():
    # Make sure that the language dataset is ready
    download_wikipedia_language_dataset()

    # Subsample the training set to make the test run fast enough.
    df = pd.read_parquet(DATA_FOLDER_PATH / "wikipedia_language.parquet")
    df_train, df_test = train_test_split(
        df, train_size=int(1e3), test_size=int(1e3), random_state=0)

    text_classifier = build_language_classifier(
        df_train["text"], df_train["language"],
        random_state=0)

    train_acc = text_classifier.score(df_train["text"], df_train["language"])
    test_acc = text_classifier.score(df_test["text"], df_test["language"])
    assert train_acc > 0.97 and test_acc > 0.95

    short_texts = [
        "Do you understand the instructions?",
        "¿Entiendes las instrucciones?",
        "Coneixes les instruccions?",
        "Comprenez-vous les instructions?",
        "Hai capito le istruzioni?",
        "Verstehst du die Anweisungen?",
    ]
    assert_array_equal(
        text_classifier.predict(short_texts),
        ["en", "es", "ca", "fr", "it", "de"],
    )


def test_language_detector_with_pretrained_model():
    language_detector = get_language_detector()
    if language_detector is None:
        pytest.skip("Missing pre-trained language detection model.")

    assert language_detector("") is None

    metadata_path = DATA_FOLDER_PATH / "poetry/metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    for poem in metadata:
        filepath = DATA_FOLDER_PATH / "poetry" / poem["filename"]
        text = filepath.read_text(encoding=poem["encoding"])
        assert language_detector(text) == poem["language"]
