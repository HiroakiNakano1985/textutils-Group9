import textutils.core as core


def test_word_lengths_pipeline():
    text = "Hello,   world!\t Our gRoup is 9. \n wE are all frIends!! This is how things are in our group."
    normalized = core.normalize_whitespace(text)
    punctuated = core.remove_punctuation(normalized)
    reversed = core.reverse_words(punctuated)
    counts = core.word_count(reversed)
    unique = core.unique_words(reversed)    
    length = core.word_lengths(reversed)
    vowels = core.count_vowels(reversed)
    assert counts == {'hello': 1, 'world': 1, 'our': 2, 'group': 2, 'is': 2, '9': 1, 'we': 1, 'are': 2, 'all': 1, 'friends': 1, 'this': 1, 'how': 1, 'things': 1, 'in': 1}
    assert unique == ['9', 'all', 'are', 'friends', 'group', 'hello', 'how', 'in', 'is', 'our', 'things', 'this', 'we', 'world']
    assert length == {'hello': 5, 'world': 5, 'our': 3, 'group': 5, 'is': 2, '9': 1, 'we': 2, 'are': 3, 'all': 3, 'friends': 7, 'this': 4, 'how': 3, 'things': 6, 'in': 2}
    assert vowels == 25