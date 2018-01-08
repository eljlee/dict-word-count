# put your code here.
def word_count(filename):
    """Taking in file, putting each unique word into a dictionary, and number of occurence as it's value"""
    the_file = open(filename)
    word_count = {}
    for line in the_file:
        line = line.rstrip().split(" ")
        for word in line:
            word_count[word] = word_count.get(word, 0) + 1
        #print word_count
    
    for word in word_count:
        print word, word_count[word]
    return word_count

word_count("test.txt")