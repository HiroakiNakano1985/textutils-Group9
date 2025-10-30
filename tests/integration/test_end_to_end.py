import textutils.core as core

#I don't still understand how each function works. Therefore, result is empty now.

def test_word_lengths_pipeline():
    text = "Hello,   world!\t My name is   Hiroaki Nakano \n We are all friends!!"
    normalized = core.normalize_whitespace(text)
    punctuated = core.remove_punctuation(normalized)
    counts = core.word_count(punctuated)
    unique = core.unique_words(punctuated)    
    length = core.word_lengths(punctuated)
    vowels = core.count_vowels(punctuated)
    assert counts ==
    assert unique ==
    assert length == {"hello": 5, "world": 5}
    assert vowels ==
