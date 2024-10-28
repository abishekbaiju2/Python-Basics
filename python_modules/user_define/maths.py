def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

def product(*args):
    product=1
    for i in args:
        product*=i
    return product

def minvalue(*args):
    min=args[0]
    for i in args:
        if min>i:
            min =i
    return min

def maxvalue(*args):
    max=args[0]
    for i in args:
        if max<i:
            max =i
    return max
