import string
def read_text(filename):
    """
    filename: string, name of file to read
    Returns a string containing all file contents
    """
    in_file = open(filename, 'r')
    line = in_file.read()
    return line

def find_words(text):
    """
    text: string
    Returns a list of words from input text
    """
    text = text.replace("\n", " ")
    for char in string.punctuation:
        text = text.replace(char, "")
    words = text.split(" ")
    return words

def frequencies(words):
    """
    words: list of words
    Returns a frequency dictionary for input words
    """
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

def calculate_similarity(d1, d2):
    """
    d1: frequency dictionary for one text
    d2: frequency dictionary for another text
    Returns a float representing how similar both
    texts are to each other
    """
    diff = 0
    total = 0
    # when word is in both dicts or just in d1
    for word in d1.keys():
        if word in d2.keys():
            diff += abs(d1[word] - d2[word])
        else:
            diff += d1[word]
    # when word is just in d2
    for word in d2.keys():
        if word not in d1.keys():
            diff += d2[word]
            
    total = sum(d1.values()) + sum(d2.values())
    similar = 1-diff/total
    return round(similar, 2)
    
text1 = read_text("sonnet18.txt")
text2 = read_text("sonnet19.txt")
#print(text)
words1 = find_words(text1)
words2 = find_words(text2)
#print(words)
freq_dict1 = frequencies(words1)
freq_dict2 = frequencies(words2)
#print(freq_dict)
print(calculate_similarity(freq_dict1, freq_dict2))

