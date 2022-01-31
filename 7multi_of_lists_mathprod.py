import math
from unittest import result

def multi_lists(items):
    total =1
    for x in items:
        total= math.prod(items)
    return total
print(multi_lists([1,2,3]))

