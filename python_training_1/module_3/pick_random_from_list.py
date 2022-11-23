# Que :  How can you pick a random item from a list or tuple? 

import random

l1=[2,32,"hello",78,"Better Luck Next Time !!!"]

print(random.choice(l1))

# Que : How will you randomizes the items of a list in place?

random.shuffle(l1)

print(l1)

# Que : How can you pick a random item from a range? 

print(random.randint(100,200))