# the random module in python is used to generate  pseudo-random datas for various purpose
# such as selecting random elements , shuffling sequences or generating random numbers in a specific range
import random

# help(random)

# generate a random integer between 10 and 20 (inclusive)

print(random.randint(10,20))

# generate a random float between 5.5 and 10.5

print(random.uniform(5.5,10.5))

# select a random element from a list

items=['apple','banana','cherry']
print(random.choice(items))

# select 2 random elements from a list

print(random.sample(items,2))

# shuffle a list in place
random.shuffle(items)
print(items)