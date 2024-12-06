# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Sort the original word and compare it with each word in the list
        return [word for word in possible_anagrams if sorted(word) == sorted(self.word)]
