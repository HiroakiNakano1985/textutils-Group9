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
