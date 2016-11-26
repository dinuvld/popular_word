class String:

    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text)

    def delete_char(self, position):
        """Takes the position of a character in a string (starting from 0) and  deletes at that position"""
        newstr = list()
        for index in range(0, position):
            newstr.append(self.text[index])
        for index in range(position + 1, len(self.text)):
            newstr.append(self.text[index])
        self.text = "".join(newstr)

    def insert_char(self, position, char):
        """Takes the position at which a charater shall be intoruced and expands the string accordingly"""
        newstr = list()
        for index in range(0, position):
            newstr.append(self.text[index])
        newstr.append(char)
        for index in range(position, len(self.text)):
            newstr.append(self.text[index])
        self.text = "".join(newstr)

    def search_for_char(self, char):
        """Searches a string for a specific character and returns a list with the positions in which that
        character is found"""
        position_list = list()
        for index in range(0, len(self.text)):
            if self.text[index] == char:
                position_list.append(index)
        return position_list

    def replace_char(self, to_replace, replacement):
        """Replace all occurrences of a character in a string with another character"""
        newstr = list()
        position_list = self.search_for_char(to_replace)
        for index in range(0, len(self.text)):
            if index not in position_list:
                newstr.append(self.text[index])
            else:
                newstr.append(replacement)
        self.text = "".join(newstr)

