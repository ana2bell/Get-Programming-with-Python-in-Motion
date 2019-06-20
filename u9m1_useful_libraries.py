##################################
####### MATH LIBRARY #############
##################################
import math              

distance = float(input("How far away is your friend? (m) "))
speed = float(input("How fast can you throw? (m/s) "))
angle_d = float(input("What angle do you want to throw at? (degrees) "))
tolerance = 2

angle_r = math.radians(angle_d)     

reach = 2*speed**2*math.sin(angle_r)*math.cos(angle_r)/9.8    

if reach > distance - tolerance and reach < distance + tolerance:
    print("Nice throw!")
elif reach < distance - tolerance:
    print("You didn't throw far enough.")
else:
    print("You threw too far.") 

##################################
####### RANDOM LIBRARY ###########
##################################
import random

people = ["Ana","Bob","Carl","Doug","Elle","Finn"]
print(random.choice(people))

people = ["Ana","Bob","Carl","Doug","Elle","Finn"]
print(random.sample(people, 3))

######## ROCK PAPER SCISSORS #####
choice = input("Choose rock, paper, or scissors: ")
r = random.random()    
if r < 1/3:          
    print("Computer chose rock.")
    if choice == "paper":
        print("You win!")
    elif choice == "scissors":
        print("You lose.")
    else:
        print("Tie.")
elif 1/3 <= r < 2/3:   
    print("Computer chose paper.")
    if choice == "scissors":
        print("You win!")
    elif choice == "rock":
        print("You lose.")
    else:
        print("Tie.")
else:         
    print("Computer chose scissors.")
    if choice == "rock":
        print("You win!")
    elif choice == "paper":
        print("You lose.")
    else:
        print("Tie.")

########## USING A SEED ###########
random.seed(0)
print(random.randint(2,17))
print(random.randint(30,88))

##################################
####### TIME LIBRARY #############
##################################
import time   

start = time.clock() 

count = 0        
for i in range(1000000):  
    count += 1    

end = time.clock() 
print(end-start) 

print("Loading...")
for i in range(10):         
    print("[",i*"*",(10-i)*" ","]",i*10,"% complete")            
    time.sleep(0.5)
