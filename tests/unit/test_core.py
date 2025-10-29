import textutils.core as c

def test_count_vowels_basic():
    text = "Hello"
    assert c.count_vowels(text) == 2

def test_count_vowels_multiple_words():
    text = "Hello professor, how are you?"
    assert c.count_vowels(text) == 10

def test_count_vowels_capital_vowels():
    text = "AAAY CARAMBAAA, please help me!"
    assert c.count_vowels(text) == 13

def test_count_vowels_no_vowels():
    text = "rhythm"
    assert c.count_vowels(text) == 0

def test_count_vowels_empty_string():
    text = ""
    assert c.count_vowels(text) == 0

import textutils.core as core

def test_reverse_words():
    text = "Red red BLUE"
    result = c.word_count(text)
    assert result == {"red": 2, "blue": 1}

def test_remove_punctuation():
    text = ""
    result = c.word_count(text)
    assert result == {}

def test_word_lengths():
    text = "hi   hi    hi\nhi"
    result = c.word_count(text)
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
