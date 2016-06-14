def word_count(str):
    words = {}
    for word in str.split():
        words[word] = words.get(word, 0) + 1
    return words