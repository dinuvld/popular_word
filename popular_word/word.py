from string import String

class Word(String):

    bad_chars = ['.', '?', '!', ':', ';', '-',
                 '(', ')', '[' ']', '"', '/', ',']

    def __init__(self, text):
        self.text = text

    def evaluate_word(self, word):
        newstr = list()
        for index in range(0, word):
            