# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
        contents_list = (contents.split())
    return contents_list

print(read_file_content("./story.txt"))

import itertools
from collections import Counter
def count_words(text):
    text_list = read_file_content(text)
    result = Counter(itertools.chain(text_list))
    return result

print(count_words("./story.txt"))
