import textutils.core as core

def test_word_count_basic():
    text = "Red red BLUE"
    result = core.word_count(text)
    assert result == {"red": 2, "blue": 1}

def test_word_count_empty_string():
    text = ""
    result = core.word_count(text)
    assert result == {}

def test_word_count_extra_spaces():
    text = "hi   hi    hi\nhi"
    result = core.word_count(text)
    assert result == {"hi": 4}


def test_word_lengths_basic():
    text = "hello world"
    result = core.word_lengths(text)
    assert result == {"hello": 5, "world": 5}


def test_word_lengths_empty_string():
    text = ""
    result = core.word_lengths(text)
    assert result == {}


def test_word_lengths_mixed_case():
    text = "Hello hELLo world"
    result = core.word_lengths(text)
    # Case-insensitive: both "Hello" and "hELLo" count as the same word length
    assert result == {"hello": 5, "world": 5}