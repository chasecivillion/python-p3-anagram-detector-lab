# your code goes here!
import ipdb

class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match(self, list_words):
        matching_word_list = []
        for word in list_words:
            if sorted([letter for letter in word]) == self.word_letters:
                matching_word_list.append(word)
        return matching_word_list