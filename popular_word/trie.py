import random
import string
import time
class Node():

    letter = ""

    def __init__(self, letter):
        self.letter = letter
        self.counter = 0
        self.next_node = list()



class Trie():


    def __init__(self):
        self.root = Node("")

    def __add_word(self, word, current_node, index, prev, change_prev):

        found = False

        if change_prev is True:
            current_node.prev_node = prev

        if index == len(word):
            current_node.counter += 1
            return

        for node in current_node.next_node:

            if node.letter == word[index]:
                found = True
                self.__add_word(word, node, index + 1, current_node, True)

        if found == False:
            current_node.next_node.append(Node(word[index]))
            self.__add_word(word, current_node, index, current_node, False)

    def __number_of_apparitions(self, word, current_node, index):

        if index == len(word):
            return current_node.counter

        for node in current_node.next_node:
            if node.letter == word[index]:
                return self.__number_of_apparitions(word, node, index + 1)

        return "error"

    def __word_from_node(self, node):
        str = ''
        if node.letter != '':
            return str + node.letter + self.__word_from_node(node.prev_node)
        return ''

    def add_word(self, word):
        self.__add_word(word, self.root, 0, self.root, True)

    def number_of_apparitions(self, word):
        return self.__number_of_apparitions(word, self.root, 0)

    def word_from_node(self, node):
        str = self.__word_from_node(node)
        return str[::-1]