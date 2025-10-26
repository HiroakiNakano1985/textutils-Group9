def unique_words(text):
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = sorted(set(words))
    return unique_words
