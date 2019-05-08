for v in range(5):
    print(v)
     
for v in range(3, 7):
    print(v)
 
for v in range(2, 10, 2):
    print(v)
    
for ch in "GO TEAM":
    if ch != " ":
        print("Let me hear you say:", ch)
    
######################
###### Quickcheck ####
######################
n = int(input("Height of the star triangle: "))

for i in range(1, n+1):
    print("*" * i)

for i in range(n-1, 0, -1):
    print("*", * i)