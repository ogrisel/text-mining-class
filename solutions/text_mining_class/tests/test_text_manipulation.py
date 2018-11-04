from text_mining_class.text_manipulation import code_points
from text_mining_class.text_manipulation import remove_accents
from text_mining_class.text_manipulation import tokenize_western_language
from text_mining_class.text_manipulation import tokenize_japanese


# TODO: write a test to detect letters vs punctuation


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


def test_remove_accents():
    assert "C'est l'ete!" == remove_accents("C'est l'été!")
    assert "Ca va bien comme ca!" == remove_accents("Ça va bien comme ça!")


def test_tokenize_western_language():
    expected = ["This", "is", "a", "test"]
    assert tokenize_western_language("This is a test.") == expected

    expected = ["C", "est", "l", "ete"]
    assert tokenize_western_language("C'est l'ete!") == expected


def test_tokenize_japanese():
    text = "古池や蛙飛び込む水の音"
    expected = ['TODO']
    assert tokenize_japanese(text) == expected
