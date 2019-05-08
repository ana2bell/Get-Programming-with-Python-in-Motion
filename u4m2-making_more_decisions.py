##### Example 1 #####
n1 = int(input("Enter a number: "))
n2 = int(input("And another: "))
 
if n1 < 0 and n2 < 0:
    print("You entered two negative numbers.")

# does the wrong thing    
if n1 == (0 and 1) == n2:
    print("You entered a zero and a one.")

##### Example 2 #####
love = False
hate = True

if love and not hate:
    print("Happy!")
elif not love and hate:
    print("Angry!")

##### Example 3 #####
if True:
    print("first")
elif True:
    print("second")
elif True:
    print("third")
    
##### Example 4 #####
n1 = int(input("Enter a number: "))
if n1 > 0:
    print("positive")
else:
    print("is zero")
    
##### Quickcheck Exercise #####
n1 = 5
n2 = 6
print("I'm thinking of 2 numbers: ")

op = input("Enter + or -: ")
if op == "+":
    print("a + b =", n1 + n2)
elif op == "-":
    print("a - b =", n1 - n2)
else:
    print("That's not a choice.")
    
op = input("Enter + or -: ")
if op == "+":
    print("a + b =", n1 + n2)
elif op == "-":
    print("a - b =", n1 - n2)
else:
    print("That's not a choice.")

a = int(input("What's a? "))
b = int(input("What's b? "))
if a == n1 and b == n2:
    print("Correct!")
else:
    print("Nope. Play again!")