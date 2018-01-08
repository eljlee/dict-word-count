# put your code here.
import string
import sys

#print sys.argv

def word_count(filename):
    """Taking in file, putting each unique word into a dictionary, and number of occurence as it's value"""
    

    the_file = open(filename)
    word_count = {}
    for line in the_file:
        words = line.rstrip().split(" ")
        for word in words:
            word = word.strip(string.punctuation).lower()
            word_count[word] = word_count.get(word, 0) + 1
        #print word_count
    
    for word in word_count:
        print word, word_count[word]
    return word_count


for text_file in sys.argv[1:]:
    word_count(text_file)