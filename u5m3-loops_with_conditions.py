text = input("Wash? YES or NO: ")
while text == "YES":
    print("Lather.")
    print("Rinse")
    text = input("Again? YES or NO: ")
    phone = input("Was that the phone? YES or NO: ")
    if phone == "YES":
        break

for i in range(5):
    print("in for loop", i)
    
i = 0
while i < 5:
    print("in while loop", i)
    i = i + 1  # alternate way is i += 1
    

for i in range(1, 11):
    if i%3 == 0:
        continue
    print(i)

#########################
## Quickcheck Exercise ##    
#########################
while True:
    pwd = input("Make up a password: ")
    # check the requirements
    longer_than_6 = (len(pwd) >= 6)
    has_capital = False
    has_digit = False
    for ch in pwd:
        if ch in "0123456789":
            has_digit = True
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_capital = True
    # tell the user they did not meet a requirement
    if not longer_than_6:
        print("Must be 6 or more characters.")
    if not has_capital:
        print("Must have at lease one capital letter.")
    if not has_digit:
        print("Must have at least one digit.")
    # conditions to ask for a new password
    if not longer_than_6 or not has_capital or not has_digit:
        continue                       
    break
print("Great password!")
