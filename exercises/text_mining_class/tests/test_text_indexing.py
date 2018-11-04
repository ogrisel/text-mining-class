from text_mining_class.text_indexing import build_index
import text_mining_class
from pathlib import Path

package_path = text_mining_class.__path__[0]
POETRY_FOLDER_PATH = Path(package_path) / 'data' / 'poetry'


def test_french_tokens():
    index = build_index(POETRY_FOLDER_PATH)

    results = sorted(index.get("automne"))
    expected_results = [
        ('baudelaire.txt', [17]),
        ('verlaine.txt', [1, 6]),
    ]
    assert results == expected_results

    results = index.get("feeriques")
    expected_results = [
        ('baudelaire.txt', [20]),
    ]
    assert results == expected_results


def test_english_tokens():
    index = build_index(POETRY_FOLDER_PATH)

    results = index.get("thy")
    expected_results = [
        ('shakespeare.txt', [7, 9, 20]),
    ]
    assert results == expected_results

    results = index.get("holly")
    expected_results = [
        ('shakespeare.txt', [11, 13, 22, 24]),
    ]
    assert results == expected_results


def test_japanese_tokens():
    index = build_index(POETRY_FOLDER_PATH)
    # TODO
