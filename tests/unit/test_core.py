import textutils.core as core

def test_reverse_words():
    text = "Red red BLUE"
    result = core.word_count(text)
    assert result == {"red": 2, "blue": 1}

def test_remove_punctuation():
    text = ""
    result = core.word_count(text)
    assert result == {}

def test_word_lengths():
    text = "hi   hi    hi\nhi"
    result = core.word_count(text)
    assert result == {"hi": 4}



def test_unique_words():
    text = "I am studying Spanish from last month."
    result = core.unique_words(text)
    assert result == ["am", "from", "i", "last", "month", "spanish" , "studying"]
    
    
    

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