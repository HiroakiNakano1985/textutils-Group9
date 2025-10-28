def word_count(text: str) -> dict[str, int]:

    counts: dict[str, int] = {}

    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1

    return counts



import string

def remove_punctuation(text):
    
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
