from string import String

class Word(String):

    bad_chars = ['.', '?', '!', ':', ';', '-',
                 '(', ')', '[' ']', '"', '/', ',']

    def __init__(self, text):
        self.text = text

    def evaluate_word(self):
        """Check in order to see if a word contains any invalid characters"""

        newstr = list()
        for index in range(0, len(self.text) - 1):
           # print len(self.text)
            #print self.text
            if (self.text[index] in self.bad_chars):
                self.delete_char(index)
                print index



str = raw_input()
str = Word(str)
str.evaluate_word()
print str.text


