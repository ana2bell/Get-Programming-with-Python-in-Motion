class Circle(object):
    def __init__(self):
        self.radius = 0
    def change_radius(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius

class Stack(object):
    def __init__(self):
        self.stack = []
    def get_stack_elements(self):
        return self.stack.copy()
    def add_one(self, item):
        self.stack.append(item)
    def remove_one(self):
        self.stack.pop()
    def add_many(self, item, n):
        for i in range(n):
            self.stack.append(item)
    def remove_many(self, n):
        for i in range(n):
            self.stack.pop()
    def size(self):
        return len(self.stack)
    def prettyprint(self):
        for thing in self.stack[::-1]:
            print('|_',thing,'_|')

pancakes = Stack()
pancakes.add_one("blueberry")
pancakes.add_many("chocolate",4)
pancakes.remove_one()
print(pancakes.size())
pancakes.prettyprint()

circles = Stack()
one_circle = Circle()
one_circle.change_radius(2)
circles.add_one(one_circle)
print(one_circle)

# add the same circle object 4 times
one_circle = Circle()
one_circle.change_radius(1)
circles.add_many(one_circle, 4)

print(circles.size())
circles.prettyprint()

circles = Stack()
one_circle = Circle()
one_circle.change_radius(2)
circles.add_one(one_circle)
print(one_circle)

# add 4 separate circle objects
for i in range(4):
    one_circle = Circle()
    one_circle.change_radius(1)
    circles.add_one(one_circle)
    
print(circles.size())
circles.prettyprint()

##############################
########## QUICKCHECK ########
##############################
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
            print('|_',thing,'_|')
            
a = Queue()
a.add_one(3)
a.add_one(1)
a.remove_one()
a.prettyprint()
