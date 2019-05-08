def read_file(file):
    """
    file: a file object
    Starting from the first line, it reads every 2 lines and stores
    them in a tuple. Starting from the second line, it reads every
    2 lines and stores them in a tuple.
    Returns a tuple of the two tuples.
    """
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0
    for line in file:
        stripped_line = line.replace("\n", "")
        # every other line starting with the first one
        if line_count % 2 == 0:
            first_every_2 += (stripped_line, )
        # every other line starting with the second one
        elif line_count % 2 == 1:
            second_every_2 += (stripped_line, )
        line_count += 1
    return (first_every_2, second_every_2)

def sanitize(some_tuple):
    """
    some_tuple: a tuple of strings
    Removes all spaces, dashes, and open/closed parentheses in each string
    Returns a tuple with cleaned up string elements
    """
    clean_string = ()
    for st in some_tuple:
        st = st.replace(" ", "")
        st = st.replace("-", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        clean_string += (st, )
    return clean_string

def analyze_friends(names, phones, all_areacodes, all_places):
    """
    names: tuple of friend names
    phones: tuple of phone numbers without special symbols
    all_areacodes: a tuple of area codes
    all_places: a tuple of states
    Prints out how many friends you have and every unique state 
    that is represented by their phone numbers.
    """
    def get_unique_area_codes():
        """
        Retunrs a tuple of all unique area codes in phones
        """
        area_codes = ()
        # phones is the parameter to analyze_friends
        for ph in phones:
            if ph[0:3] not in area_codes:
                area_codes += (ph[0:3], )
        return area_codes
    
    def get_states(some_areacodes):
        """
        some_areacodes: tuple of area codes
        Returns a tuple of the states associated with some_areacodes
        """
        states = ()
        for ac in some_areacodes:
            if ac not in all_areacodes:
                states += ("BAD AREACODE", )
            else:
                # use index to match area code with a state
                index = all_areacodes.index(ac)
                states += (all_places[index], )
        return states
    
    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)
    
    print("You have", num_friends, "friends!")
    print("They live in: ")
    for s in unique_states:
        print(s)
        

friends_file = open("friends.txt")
map_file = open("map_areacodes_states.txt")
(names, phones) = read_file(friends_file)
(areacodes, places) = read_file(map_file)
friends_file.close()
map_file.close()
#print(names)
#print(phones)
clean_phones = sanitize(phones)
#print(clean_phones)
analyze_friends(names, clean_phones, areacodes, places)
