from tmclass_exercises.text_encoding import count_bytes
from tmclass_exercises.text_encoding import text_in_bytes
from tmclass_exercises.text_encoding import count_bytes_in_file
from tmclass_exercises.text_encoding import text_in_file
from tmclass_exercises import POETRY_FOLDER_PATH
import pytest


def test_count_bytes():
    assert count_bytes(b"") == 0
    assert count_bytes(b"123") == 3
    assert count_bytes(b"abc") == 3

    assert count_bytes(bytes([])) == 0
    assert count_bytes(bytes([97, 98, 99])) == 3

    assert count_bytes("abc".encode("ascii")) == 3
    assert count_bytes("é".encode("iso-8859-1")) == 1
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
    assert count_bytes_in_file(POETRY_FOLDER_PATH / 'basho.txt') == 81
    assert count_bytes_in_file(POETRY_FOLDER_PATH / 'baudelaire.txt') == 1194
    assert count_bytes_in_file(POETRY_FOLDER_PATH / 'shakespeare.txt') == 655


def test_text_in_files():
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
