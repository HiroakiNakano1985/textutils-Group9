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
    
    
    

def test_remove_punctuation_basic():
    from textutils import core
    text = "Hello, world!"
    result = core.remove_punctuation(text)
    assert result == "Hello world"

def test_remove_punctuation_mixed():
    from textutils import core
    text = "Hi!!! It's... me???"
    result = core.remove_punctuation(text)
    assert result == "Hi Its me"

def test_remove_punctuation_numbers():
    from textutils import core
    text = "Wow, 123!!!"
    result = core.remove_punctuation(text)
    assert result == "Wow 123"
