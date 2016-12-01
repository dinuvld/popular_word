# -*- coding: utf-8 -*-
from string import String

class Word(String):

    bad_chars = ['.', '?', '!', ':', ';', '-',
                 '(', ')', '[' ']', '"', '/', ',', '”',
                 '*', '#']

    def __init__(self, text):
        self.text = text
        self.bad_chars.append(range(0, 9))

    def evaluate_word(self):
        """Check in order to see if a word contains any invalid characters"""

        newstr = list()
        index = 0
        while index < len(self.text):
            if (self.text[index] in self.bad_chars):
                self.delete_char(index)
                index = index - 1
            index = index + 1


