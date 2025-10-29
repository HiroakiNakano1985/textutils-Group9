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



import string

def remove_punctuation(text):
    
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count