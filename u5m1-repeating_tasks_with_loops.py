print("echo")
print("echo")
print("echo")
print("echo")

for i in range(4):
    print("echo")

for counter in range(4):
    print(counter, "echo")

##########################    
#### Quickcheck ##########    
##########################    
word = input("What word to spell? ")
N = len(word)

for i in range(N):
    print(i+1,":",word[i])
