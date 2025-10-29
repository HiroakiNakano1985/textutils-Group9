# textutils-Group9>
 A small collaborative Python package that provides simple text utilities.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HiroakiNakano1985/textutils-9.git
   cd textutils-9
```


2. Create the environment (with micromamba):

   ```bash
   micromamba create -f environment.yml -y
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
* `will complete later` → collapses multiple spaces/newlines into one
* `normalize_whitespace(text)` → collapses multiple spaces/newlines into one

## Team

HiroakiNakano1985
engpongtanya-16
leomatthey
maryemeidiata
MateoBarredaR
