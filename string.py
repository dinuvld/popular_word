import search

class String:

    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def remove_char(self, position):
        """Takes the position of a character in a string (starting from 0) and  deletes at that position"""
        newstr = list()
        for index in range(0, position):
            newstr.append(self.string[index])
        for index in range(position + 1, len(self.string)):
            newstr.append(self.string[index])
        self.string = "".join(newstr)



