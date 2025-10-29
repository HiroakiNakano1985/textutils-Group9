import textutils.core as core
def test_word_lengths_pipeline():
    text = "Hello,   world!"
    normalized = core.normalize_whitespace(text)
    result = core.word_lengths(normalized)
    assert result == {"hello": 5, "world": 5}
