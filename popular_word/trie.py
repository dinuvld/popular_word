#from exceptions import WordNotInDictionary

class Node():

    letter = ""
    prev_letter = ""

    def __init__(self, letter):
        self.letter = letter
        self.counter = 0
        self.next_node = list()



class Trie():


    def __init__(self):
        self.root = Node("")

    def __add_word(self, word, current_node, index):

        if index == len(word):
            current_node.counter += 1
            return

        found = False
        for node in current_node.next_node:
            if node.letter == word[index]:
                found = True
                self.__add_word(word, node, index + 1)

        if found == False:
            current_node.next_node.append(Node(word[index]))
            self.__add_word(word, current_node, index)


    def __number_of_apparitions(self, word, current_node, index):

        if index == len(word):
            return current_node.counter

        for node in current_node.next_node:
            if node.letter == word[index]:
                return self.__number_of_apparitions(word, node, index + 1)

        return "error"


    def add_word(self, word):
        self.__add_word(word, self.root, 0)

    def number_of_apparitions(self, word):
        return self.__number_of_apparitions(word, self.root, 0)




