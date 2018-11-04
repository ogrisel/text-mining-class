from text_mining_class.text_encoding import list_text_files
from text_mining_class.text_encoding import count_bytes
import text_mining_class
from pathlib import Path

package_path = text_mining_class.__path__[0]
POETRY_FOLDER_PATH = Path(package_path) / 'data' / 'poetry'


def test_count_words():
    pass


def test_list_text_files():
    text_filepaths = list_text_files(POETRY_FOLDER_PATH)

    expected = ['basho.txt', 'baudelaire.txt', 'shakespeare.txt']
    assert [p.name for p in text_filepaths] == expected


def test_count_bytes_in_files():
    assert count_bytes(POETRY_FOLDER_PATH / 'basho.txt') == 81
    assert count_bytes(POETRY_FOLDER_PATH / 'baudelaire.txt') == 1194
    assert count_bytes(POETRY_FOLDER_PATH / 'shakespeare.txt') == 655
