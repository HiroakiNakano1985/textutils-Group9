from __future__ import annotations
import re
import string
from typing import Dict

def unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = sorted(set(words))
    return unique_words

def word_count(text: str) -> dict[str, int]:

    counts: dict[str, int] = {}

    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1

    return counts

def remove_punctuation(text):
    
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def word_lengths(text: str) -> Dict[str, int]:
    """
    Return {word_lowercase: length} for each distinct word (case-insensitive).
    Strips simple punctuation around words.
    Empty input -> {}.
    """
    text = normalize_whitespace(text)
    if not text:
        return {}

    out: Dict[str, int] = {}
    for w in text.split():
        # strip leading/trailing non-word chars, then lower
        lw = re.sub(r"^\W+|\W+$", "", w.lower())
        if lw:                      # skip tokens that become empty
            out[lw] = len(lw)
    return out

def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# Code for reverse_words
def reverse_words(text: str) -> str:
    """
    Reverse the order of words in a given text.
    Words are separated by any whitespace.
    Extra spaces are ignored.
    """
    # Split by any whitespace, remove empties
    words = text.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join them back into a single space-separated string
    return " ".join(reversed_words)