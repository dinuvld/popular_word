# -*- coding: utf-8 -*-
from _string import String

class Word(String):

    bad_chars = ['.', '?', '!', ':', ';', '-',
                 '(', ')', '[' ']', '"', '/', ',', '”',
                 '*', '#', '\'']
    sentence_end = ['.', '!', '?']

    def __init__(self, text):
        self.text = text
        self.bad_chars.append(range(0, 9))

    def __should_delete_char(self, text, position):
        """Test to see if the char at position should be deleted, returns True, if it should, False if not
        (it it's at the end of the word with multiple other illegal characters afterwards, it should,
         if it's at the middle of the word, followed by legal characters, it shouldn't) """

        if text[position] in self.bad_chars:
            if position == len(text) - 1:
                return True
            elif position == 0:
                return True
            elif text[position + 1] in self.bad_chars:
                return True
        return False

    def check_for_sentence_end(self):
        """Check for a singular '.' in order to assert the word is the end of the sentence.
        Should make sure that the '.' is not part of strings such as '...', or part in an abbreviation
        that doesn't mark the end of the sentence"""

        text_length = len(self.text)
        first = True

        for index in range(0, text_length):
            if self.text[index] in self.sentence_end:
                if first is True and index == text_length - 1:
                    return True
                else:
                    return False
        return False

    def evaluate_word(self):
        """Check in order to see if a word contains any invalid characters, delete
        any invalid chars"""

        index = 0
        text_length = len(self.text)
        while index < text_length:
            if self.__should_delete_char(self.text, index):
                self.delete_char(index)
                text_length -= 1
                index -= 1
            index += 1



