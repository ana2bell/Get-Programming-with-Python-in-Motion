############################
###### Fraction class ######
############################
class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __add__(self, other_fraction):
        # new numerator and denominator use self's and other_fraction's 
        # numerators and denominators (top and bottom data attributes)
        new_top = self.top*other_fraction.bottom  +  \
                  self.bottom*other_fraction.top 
        new_bottom = self.bottom*other_fraction.bottom
        return Fraction(new_top, new_bottom)   
    def __mul__(self, other_fraction):
        new_top = self.top*other_fraction.top
        new_bottom = self.bottom*other_fraction.bottom
        return Fraction(new_top, new_bottom)
    def __str__(self):                                     
        return str(self.top)+"/"+str(self.bottom)      

half = Fraction(1,2)
quarter = Fraction(1,4)
print(half + quarter)
print(half.__add__(quarter))
print((half.__add__(quarter)).__str__())

############################
######### Queue class ######
############################
class Queue(object):
    def __init__(self):
        self.queue = []
    def get_queue_elements(self):
        return self.queue.copy()
    def add_one(self, item):
        self.queue.append(item)
    def remove_one(self):
        self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def prettyprint(self):
        for thing in self.queue[::-1]:
            print('|_',thing, '_|')
    def __str__(self):
        ret = ""
        for thing in self.queue[::-1]:
            ret += ('|_ '+str(thing)+ ' _|\n')
        return ret

a = Queue()
a.add_one(3)
a.add_one(2)
a.add_one(1)
print(a)
