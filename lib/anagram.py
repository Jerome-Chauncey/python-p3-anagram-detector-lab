class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        matched_anagrams = []
        sort_original_word = sorted(self.word)

        for each_word in list:
            if sorted(each_word) == sort_original_word and each_word.lower() != self.word.lower():
                matched_anagrams.append(each_word)


        return matched_anagrams
    
anagram = Anagram("listen")
print(anagram.match(['enlists', 'google', 'inlets', 'banana', 'netsil']))
print(anagram.word)
