import pytest
from tmclass_exercises.text_manipulation import code_points
from tmclass_exercises.text_manipulation import character_categories
from tmclass_exercises.text_manipulation import remove_accents
from tmclass_exercises.text_manipulation import tokenize_generic
from tmclass_exercises.text_manipulation import tokenize_japanese


def test_code_points():
    assert code_points("ABC") == [65, 66, 67]
    assert code_points("abc") == [97, 98, 99]
    assert code_points("123") == [49, 50, 51]
    assert code_points(".,:") == [46, 44, 58]
    assert code_points("中国語") == [20013, 22269, 35486]
    assert code_points("☃⛄⛇") == [9731, 9924, 9927]


def test_unicode_normalization():
    assert code_points("Ça va", normalize="NFC") == [199, 97, 32, 118, 97]
    assert code_points("Ça va", normalize="NFD") == [67, 807, 97, 32, 118, 97]


def test_character_category():
    text = "C’est l’été 2018!"
    categories = character_categories(text)
    assert len(categories) == len(text)
    assert categories == [
        "Lu", "Pf", "Ll", "Ll", "Ll", "Zs",  # "C'est "
        "Ll", "Pf", "Ll", "Ll", "Ll", "Zs",  # "l’été "
        "Nd", "Nd", "Nd", "Nd", "Po"]        # "2018!"

    categories = character_categories(text, normalize="NFD")
    assert len(categories) == len(text) + 2  # 2 accents
    assert categories == [
        "Lu", "Pf", "Ll", "Ll", "Ll", "Zs",              # "C'est "
        "Ll", "Pf", "Ll", "Mn", "Ll", "Ll", "Mn", "Zs",  # "l’été "
        "Nd", "Nd", "Nd", "Nd", "Po"]                    # "2018!"


def test_remove_accents():
    assert "C’est l’ete!" == remove_accents("C’est l’été!")
    assert "Ca va bien comme ca!" == remove_accents("Ça va bien comme ça!")


def test_tokenize_generic():
    text = "This is a test."
    expected = ["This", "is", "a", "test"]
    assert tokenize_generic(text) == expected

    text = "42 is a number."
    expected = ["42", "is", "a", "number"]
    assert tokenize_generic(text) == expected

    text = "C’est l’ete!"
    expected = ["C", "est", "l", "ete"]
    assert tokenize_generic(text) == expected

    text = "C’est l’été!"
    expected = ["C", "est", "l", "été"]
    assert tokenize_generic(text) == expected


def test_tokenize_persian():
    text = "ای باغبان ای باغبان آمد خزان آمد خزان"
    expected = ["ای", "باغبان", "ای", "باغبان", "آمد", "خزان", "آمد", "خزان"]
    assert tokenize_generic(text) == expected


def test_tokenize_japanese():
    pytest.importorskip('janome')  # skip this test if janome is not installed

    text = "古池や蛙飛び込む水の音"
    expected = ['古池', 'や', '蛙', '飛び込む', '水', 'の', '音']
    assert tokenize_japanese(text) == expected
