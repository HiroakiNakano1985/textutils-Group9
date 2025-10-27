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
