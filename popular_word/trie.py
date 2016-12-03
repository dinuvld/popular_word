from word import Word

class Node():

    string = ""
    prev_node = ""
    next_node = list()

    def __init__(self, string):
        self.string = string



class Trie():

    nodes = list()

    def __init__(self):
        self.nodes.append(Node(''))

    def add_word(self, word):
        for index in range(0, len(word)):
            if word[index] in self.nodes:

