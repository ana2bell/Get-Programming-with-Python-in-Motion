a = 1
id(a)
b = a
id(b)
a = 2
id(a)
id(b)

genius = ["einstein", "galileo"]
id(genius)
smart = genius
id(smart)
genius.append("shakespeare")
id(genius)
id(smart)
genius
smart

def add_word(d, word, definition):	
    """ d, dict that maps strings to lists of strings
        word, a string
        definition, a string
        Mutates d by adding the entry word:definition
        If word is already in d, append definition to word’s value list
        Does not return anything
    """
    if word in d:				
        d[word].append(definition)	
    else:					
        d[word] = [definition]		

words = {}				
add_word(words, 'box', 'fight')	
print(words)				
add_word(words, 'box', 'container')	
print(words)				
add_word(words, 'ox', 'animal')	
print(words)	

artists = ["monet", "picasso"]
painters = list(artists)
print(artists)
print(painters)
painters.append("van gogh")
print(painters)
print(artists)

artists = ["monet", "picasso"]
painters = artists.copy()
painters.append("van gogh")
print(painters)
print(artists)

kid_ages = [2, 1, 4]
sorted_ages = sorted(kid_ages)
print(sorted_ages)
print(kid_ages)

songs = {"Wannabe":1, "Roar":1, "Let It Be":5, "Red Corvette":4}

# incorrect way to remove songs with a rating of 1
#for s in songs.keys():
#    if songs[s] == 1:
#        songs.pop(s)
#print(songs)

# incorrect way to remove songs with a rating of 1
songs = [1,1,5,4]

for s in songs:
    if s == 1:
        songs.remove(s)
print(songs)

# correct way to remove songs with a rating of 1
songs = [1,1,5,4]
songs_copy = songs.copy()
songs = []

for s in songs_copy:
    if s != 1:
        songs.append(s)
print(songs)
