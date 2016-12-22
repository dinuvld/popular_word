import os, glob

dir = os.chdir('/Users/vlad/Developer/popular_word/texts')

for file in glob.glob('sherlock.txt'):
    f = open(file, 'r')
    for word in f:
        print word
        break