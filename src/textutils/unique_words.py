def unique_words(text):
    #have to add "delete anything that's not a word character or whitespace"

    words = text.lower().split()

    return sorted(set(words))
