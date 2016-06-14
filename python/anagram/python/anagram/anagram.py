from collections import Counter

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return word1 != word2 and \
        len(word1) == len(word2) and \
        Counter(word1) == Counter(word2)


def detect_anagrams(word, words):
    return filter(lambda other_word: is_anagram(word, other_word), words)