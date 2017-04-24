import os, glob
import trie, word

dir = os.chdir('/Users/vladdinu/Developer/popular_word/popular_word/texts')
tree = trie.Trie()

for file in glob.glob('test.txt'):
    f = open(file, 'r')
    for sentence in f:
        #print sentence
        words = sentence.split()
        for string in words:
            text = word.Word(string)
            text.evaluate_word()
            text.lowercase()
            tree.add_word(text.text)
            tree.find_maximum()

for node in tree.max:
    print tree.word_from_node(node)
