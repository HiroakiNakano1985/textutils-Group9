def unique_words(text):
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = sorted(set(words))
    return unique_words

def word_count(text: str) -> dict[str, int]:

    counts: dict[str, int] = {}

    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1

    return counts
