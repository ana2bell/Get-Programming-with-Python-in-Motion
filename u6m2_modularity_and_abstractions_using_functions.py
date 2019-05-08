#########################
# Function Example ######
#########################
def get_full_length(words):
    """ 
    words: a tuple containing string elements
    Returns the toal number of characters over 
    all elements in words
    """
    length = 0
    for word in words:
        length += len(word)
    return length
    print("this never gets printed")
    
w = ("hello", "it's", "me")
print(get_full_length(w))


###############################
# Functions returning a tuple #
###############################
def add_sub(n1, n2):
    """
    n1: an int or float
    n2: an int or float
    Returns a tuple whose first element is the addition
    of n1 and n2, and whose second element is the 
    subtraction of n1 and n2
    """
    add = n1 + n2
    sub = n1 - n2
    return (add, sub)

(a,b) = add_sub(3,4)

print(a)
print(b)

##############################
# Functions without a return #
##############################
def say_name(kid):
	print(kid)
 
 
def show_kid(kid):
	return kid
 
say_name("Dora")
show_kid("Ellie")
print(say_name("Frank"))
print(show_kid("Gus"))

####################
### Quickcheck #####
####################
def seat_at_tables(group):
    """
    group: an int
    Given 3 tables of size 6 and 3 tables of size 4,
    return True if the group can be seated so that they
    completely fill any combination of tables.
    Return False if not. 
    """
    big_size = 6
    big_count = 3
    small_size = 4
    small_count = 3
    
    possible = ()
    
    for i in range(big_count + 1):
        for j in range(small_count + 1):
            possible += (i*big_size + j*small_size, )
            
    return group in possible

print(seat_at_tables(11))
