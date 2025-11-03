# textutils-Group9
![Python](https://img.shields.io/badge/python-3.11-blue)  
 A small collaborative Python package that provides simple text utilities.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HiroakiNakano1985/textutils-Group9.git
cd textutils-Group9
```

2. Create the environment (with micromamba):
```bash
micromamba create -f environmentMAC.yml -y
micromamba activate textutils
```

3. Install the package in editable mode:

```bash
pip install -e .
```

## Running Tests

To run all tests and check coverage:

```bash
pytest
```

To see detailed coverage information:

```bash
pytest --cov=src/textutils --cov-report=term-missing
```

## Features

* `unique_words(text)` → returns a sorted list of distinct words (case-insensitive)
* `word_count(text)` → case-insentive counts
* `remove_punctuation(text)` → strip punctuation while keeping spaces and letters
* `normalize_whitespace(text)` → collapse runs of whitespace, trim ends
* `word_lengths(text)` → return a direct mapping words to their lengths
* `count_vowels(text)` → count vowels in the given text
* `reverse_words(text)` → reverse the order of words, not charactors


## Team

HiroakiNakano1985  
engpongtanya-16  
leomatthey  
maryemeidiata  
MateoBarredaR  
