grocery = {}
grocery = { "milk":1 , "eggs" : 12 , "bread" : 2 }
grocery = {"eggs" : (1, "carton") }
grocery = {"eggs" : (12, "individual") }

legs = {}
legs["human"] = 2
legs["cat"] = 4
legs["snake"] = 0
print(legs)
print(len(legs))

legs["cat"] = 3
print(len(legs))
print(legs)

household = {"person": 4, "cat":2, "dog":1, "fish":2 }
removed = household.pop("fish")
print(removed)
print(household)

household["fish"] = household["fish"] - 1
print(household)
 
songs = {"believe":3, "roar":5, "let it be":4}
print(songs.keys())

for one_song in songs.keys():
    print(one_song)
    
all_songs = list(songs.keys())
print(all_songs)

for one_rating in songs.values():
    print(one_rating)
    
lyrics = "Happy birthday to you Happy birthday to you Happy birthday dear friend Happy birthday to you"
counts = {}
words = lyrics.split(" ")
for w in words:
    w = w.lower()
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

print(counts)

#########################################
########### QUICKCHECK ##################
#########################################
grades = {}
grades["Chris"] = [100, 70]
grades["Angela"] = [90, 100]
grades["Bruce"] = [80, 40]
grades["Stacey"] = [70, 70]

for student in grades.keys():
    print(student)

for quizzes in grades.values():
    print(sum(quizzes)/2)

for student in grades.keys():
    scores = grades[student]
    grades[student].append(sum(scores)/2)
    
print(grades)
