from text_mining_class.text_encoding import list_text_files
import text_mining_class
from pathlib import Path

package_path = text_mining_class.__path__[0]
POETRY_FOLDER_PATH = Path(package_path) / 'data' / 'poetry'


def test_list_text_files():
    text_filepaths = list_text_files(POETRY_FOLDER_PATH)

    expected = ['basho.txt', 'baudelaire.txt', 'shakespeare.txt']
    assert [p.name for p in text_filepaths] == expected


def test_count_bytes_in_files():
    pass


def test_count_lines_in_files():
    pass


def test_count_words():
    pass


# def test_remove_western_accents():
#     assert "C'est l'ete!" == remove_accents("C'est l'été!")
#     assert "Ca va bien comme ca!" == remove_accents("Ça va bien comme ça!")
