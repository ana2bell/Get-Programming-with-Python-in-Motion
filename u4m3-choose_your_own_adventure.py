print("You're in a dark cave.")
print("Try to survive until rescue arrives!")
print("All available commands are in CAPITAL LETTERS.")
print("Any other command exits the program.")
text = input("First LOOK around... ")
if text == "LOOK":
    text = input("LEFT you hear rustling. RIGHT you see a light. ")
    if text == "LEFT":
        print("A snake bites you! You're dead =(")
    elif text == "RIGHT":
        text = int(input("How many steps will you walk? "))
        if text == 0:
            print("You stay put and miss the rescue plane =(")
        elif text < 5:
            text = input("You see BERRIES and LEAVES to eat. ")
            if text == "BERRIES":
                text = input("EAT them or NOT? ")
                if text == "EAT":
                    print("Should not have. They make you sick =(")
                elif text == "NOT":
                    text = input("A plane! MAKE a FIRE or run to a CLEARING? ")
                    if text == "FIRE":
                        print("You took too long =(")
                    elif text == "CLEARING":
                        print("They see you. You're saved!!")
                    else:
                        print("Only type in commands in CAPITAL LETTERS.")
                else:
                    print("Only type in commands in CAPITAL LETTERS.")
            elif text == "LEAVES":
                text = input("Maybe boil them for a tea. Use OCEAN or PUDDLE water? ")
                if text == "OCEAN":
                    print("A little salty, but ok. You stay hydrated and live!!")
                elif text == "PUDDLE":
                    print("You fall ill, and miss the rescue plane =(")
                else:
                    print("Only type in commands in CAPITAL LETTERS.")
            else:
                print("Only type in commands in CAPITAL LETTERS.")
        elif text >= 5:
            print("You walked off a cliff =(")
        else:
            print("You didn't follow the commands.")
    else:
        print("Only type in commands in CAPITAL LETTERS.")
else:
    print("Only type in commands in CAPITAL LETTERS.")

