import shutil
import json

from tmclass_solutions.encoding import count_bytes
from tmclass_solutions.encoding import text_in_bytes
from tmclass_solutions.encoding import count_bytes_in_file
from tmclass_solutions.encoding import text_in_file
from tmclass_solutions.encoding import convert_text_file
from tmclass_solutions import DATA_FOLDER_PATH
from tmclass_solutions import POETRY_FOLDER_PATH
import pytest


def test_count_bytes():
    assert count_bytes(b"") == 0
    assert count_bytes(b"123") == 3
    assert count_bytes(b"abc") == 3

    assert count_bytes(bytes([])) == 0
    assert count_bytes(bytes([97, 98, 99])) == 3

    assert count_bytes("abc".encode("ascii")) == 3
    assert count_bytes("é".encode("iso-8859-1")) == 1
    assert count_bytes("é".encode("iso-8859-15")) == 1
    assert count_bytes("é".encode("utf-8")) == 2


def test_count_bytes_on_invalid_input():
    with pytest.raises(TypeError):
        count_bytes("abc")


def test_text_in_bytes():
    assert text_in_bytes("abc", b"abc", encoding='ascii')
    assert text_in_bytes("abc", bytes([97, 98, 99]), encoding='ascii')

    assert text_in_bytes("abc", b"abc", encoding='utf-8')
    assert text_in_bytes("abc", b"abc", encoding='iso-8859-1')

    assert text_in_bytes("été", b'\xe9t\xe9', encoding="iso-8859-15")
    assert text_in_bytes("été", b'\xc3\xa9t\xc3\xa9', encoding="utf-8")

    binary_data = b"\xd8\xa8\xd8\xa7\xd8\xba\xd8\xa8\xd8\xa7\xd9\x86"
    assert text_in_bytes("باغبان", binary_data, encoding="utf-8")


def test_count_bytes_in_files():
    basho = POETRY_FOLDER_PATH / 'basho.txt'
    assert count_bytes_in_file(basho) == basho.stat().st_size

    baudelaire = POETRY_FOLDER_PATH / 'baudelaire.txt'
    assert count_bytes_in_file(baudelaire) == baudelaire.stat().st_size

    shakespeare = POETRY_FOLDER_PATH / 'shakespeare.txt'
    assert count_bytes_in_file(shakespeare) == shakespeare.stat().st_size


def test_text_in_files():
    # English letters without accents are encoded exactly the same way in
    # many encoding / charsets, ascii being the common subset:
    text = "winter"
    filepath = POETRY_FOLDER_PATH / 'shakespeare.txt'
    assert text_in_file(text, filepath, encoding="ascii")
    assert text_in_file(text, filepath, encoding="utf-8")
    assert text_in_file(text, filepath, encoding="iso-8859-1")

    text = "églogues"
    filepath = POETRY_FOLDER_PATH / 'baudelaire.txt'
    assert text_in_file(text, filepath, encoding="iso-8859-15")

    text = "古池や蛙飛び込む水の音"
    filepath = POETRY_FOLDER_PATH / 'basho.txt'
    assert text_in_file(text, filepath, encoding="shift-jis")
    assert not text_in_file(text, filepath, encoding="iso-8859-15")


def test_convert_files_to_utf8():
    output_path = DATA_FOLDER_PATH / "poetry_utf8"
    # Delete the test output folder and its contents if it already exists.
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir()

    with open(POETRY_FOLDER_PATH / "metadata.json") as f:
        source_metadata = json.load(f)

    for entry in source_metadata:
        filename = entry["filename"]
        source_encoding = entry["encoding"]

        source_filepath = POETRY_FOLDER_PATH / filename
        target_filepath = output_path / filename

        convert_text_file(source_filepath, source_encoding,
                          target_filepath, target_encoding="utf-8")

    # Check that all the files have been created in the output folder
    filenames = sorted([path.name for path in output_path.glob("*.txt")])
    assert filenames == ["basho.txt", "baudelaire.txt", "rumi.txt",
                         "shakespeare.txt", "verlaine.txt"]

    # Make some checks
    text = "églogues"
    filepath = output_path / 'baudelaire.txt'
    assert filepath.exists()
    assert text_in_file(text, filepath, encoding="utf-8")

    text = "古池や蛙飛び込む水の音"
    filepath = output_path / 'basho.txt'
    assert text_in_file(text, filepath, encoding="utf-8")

    text = "باغبان"
    filepath = output_path / 'rumi.txt'
    assert text_in_file(text, filepath, encoding="utf-8")

    text = "winter"
    filepath = output_path / 'shakespeare.txt'
    assert text_in_file(text, filepath, encoding="utf-8")
