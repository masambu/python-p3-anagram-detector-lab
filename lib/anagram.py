# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word 
        self.sorted_word = sorted(word) 

    def match(self, word_list):
        return [x for x in word_list if sorted(x) == self.sorted_word] or [] 
        

bobby = Anagram('lien')
print(bobby.match(['enlists', 'google', 'inlets', 'banana']))