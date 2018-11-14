import pytest
import json

from tmclass_solutions.text_indexing import TextIndex
from tmclass_solutions import POETRY_FOLDER_PATH

with open(POETRY_FOLDER_PATH / 'metadata.json') as f:
    POETRY_METADATA = json.load(f)


def test_preprocess_text():
    index = TextIndex()

    # The index object can preprocess French text to put everything in lower
    # case and remove the accentuated characters.
    preprocessed = index.preprocess("C'est l'été !", language='fr')
    assert preprocessed == "c'est l'ete !"

    # English text is transformed to lower case: there is no accentuated
    # characters to "normalize".
    preprocessed = index.preprocess("Winter is coming!", language='en')
    assert preprocessed == "winter is coming!"

    # Persian and Japanese texts are unaffected by our proprocessing.
    preprocessed = index.preprocess("ای باغبان", language="fa")
    assert preprocessed == "ای باغبان"

    preprocessed = index.preprocess("古池や蛙飛び込む水の音", language="ja")
    assert preprocessed == "古池や蛙飛び込む水の音"


def test_tokenize_text():
    index = TextIndex()
    tokens = index.tokenize("winter is coming!", language="en")
    assert tokens == ["winter", "is", "coming"]

    tokens = index.tokenize("ای باغبان", language="fa")
    assert tokens == ["ای", "باغبان"]


def test_index_text():
    index = TextIndex()
    index.index_text("doc1", "winter is coming!", language="en")
    index.index_text("doc2", "ای باغبان", language="fa")

    assert index.lookup_token("باغبان") == [('doc2', [1])]
    assert index.lookup_token("winter") == [('doc1', [1])]


def test_index_french_text_files():
    index = TextIndex()
    index.index_text_file(POETRY_FOLDER_PATH / 'baudelaire.txt',
                          language="fr", encoding="iso-8859-15")
    index.index_text_file(POETRY_FOLDER_PATH / 'verlaine.txt',
                          language="fr", encoding="utf-8")

    # Note that the following does not retrieve the occurence of the word
    # "automnes" from baudelaire.txt because we did not implement any
    # normalization strategy for plural forms. This minimal full-text index
    # could be improved in that respect.
    results = index.lookup_token("automne")
    expected_results = [
        ('verlaine.txt', [1, 6]),
    ]
    assert results == expected_results

    # Common words can return many results in many documents.
    results = index.lookup_token("mon")
    expected_results = [
        ('baudelaire.txt', [26, 26, 29]),
        ('verlaine.txt', [7]),
    ]
    assert results == expected_results

    # Token with accents are "normalized" to make it easy to query for
    # documents without having to type the accents.
    results = index.lookup_token("feeriques")
    expected_results = [
        ('baudelaire.txt', [20]),
    ]
    assert results == expected_results

    # Words not present in the indexed documents cannot be found as indexed
    # tokens:
    assert index.lookup_token("inexistant") == []


def test_index_english_text_files():
    index = TextIndex()
    index.index_text_file(POETRY_FOLDER_PATH / 'shakespeare.txt',
                          language="en", encoding="utf-8")

    results = index.lookup_token("thy")
    expected_results = [
        ('shakespeare.txt', [7, 9, 20]),
    ]
    assert results == expected_results

    results = index.lookup_token("holly")
    expected_results = [
        ('shakespeare.txt', [11, 13, 22, 24]),
    ]
    assert results == expected_results


def test_index_persian_text_files():
    index = TextIndex()
    index.index_text_file(POETRY_FOLDER_PATH / 'rumi.txt',
                          language="fa", encoding="utf-8")
    results = index.lookup_token("خزان")
    expected_results = [
        ('rumi.txt', [1, 1, 61]),
    ]
    assert results == expected_results


def test_index_japanese_text_files():
    pytest.importorskip("janome")  # skip this test if janome is not installed

    index = TextIndex()
    index.index_text_file(POETRY_FOLDER_PATH / 'basho.txt',
                          language="ja", encoding="shift-jis")
    results = index.lookup_token("蛙")
    expected_results = [
        ('basho.txt', [1]),
    ]
    assert results == expected_results


def test_complex_queries():
    index = TextIndex()
    index.index_text_file(POETRY_FOLDER_PATH / 'basho.txt',
                          language="ja", encoding="shift-jis")
    index.index_text_file(POETRY_FOLDER_PATH / 'baudelaire.txt',
                          language="fr", encoding="iso-8859-15")
    index.index_text_file(POETRY_FOLDER_PATH / 'rumi.txt',
                          language="fa", encoding="utf-8")
    index.index_text_file(POETRY_FOLDER_PATH / 'shakespeare.txt',
                          language="en", encoding="utf-8")
    index.index_text_file(POETRY_FOLDER_PATH / 'verlaine.txt',
                          language="fr", encoding="utf-8")

    assert index.query("feeriques palais", language="fr") == ["baudelaire.txt"]
    assert index.query("Féeriques palais!", language="fr") == ["baudelaire.txt"]
    assert index.query("Winter Bite", language="en") == ["shakespeare.txt"]
