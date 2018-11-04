from text_mining_class.text_encoding import list_text_files
from text_mining_class.text_encoding import count_bytes
from text_mining_class.utils import load_encoding_metadata
from text_mining_class import POETRY_FOLDER_PATH


def test_list_text_files():
    text_filepaths = list_text_files(POETRY_FOLDER_PATH)

    expected = ['basho.txt', 'baudelaire.txt', 'shakespeare.txt',
                'verlaine.txt']
    assert [p.name for p in text_filepaths] == expected


def test_count_bytes_in_files():
    assert count_bytes(POETRY_FOLDER_PATH / 'basho.txt') == 81
    assert count_bytes(POETRY_FOLDER_PATH / 'baudelaire.txt') == 1194
    assert count_bytes(POETRY_FOLDER_PATH / 'shakespeare.txt') == 655


def test_convert_to_utf8():
    encodings = load_encoding_metadata(POETRY_FOLDER_PATH / 'metadata.json')
    # TODO

