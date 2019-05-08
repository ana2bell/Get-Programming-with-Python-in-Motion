#### Example 1 #####
name = input("What's your name?")
if len(name) <= 1:
    print("I don't believe that.")
if name.count("z") == 0:
    print("No z's in your name.")
    
#### Example 2 #####
name = input("What's your name?")
if len(name) > 1:
    print("Nice name.")
    if name.islower():
        print("But why is it lowercase?")

#### Quickcheck Exercise #####
age = int(input("What's your age? "))
if age < 0:
    print("You can't be negative years old!")
if age > 100:
    print("Wow!")
if 0 <= age <= 100:
    print("You were born",age,"years ago!")
    