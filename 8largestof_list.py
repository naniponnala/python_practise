def largest(list_items):
    larger = 0
    for x in list_items:
        if x> larger:
            larger = x
    return larger
print("the larger number is",largest([1,3,4]))