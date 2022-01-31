def smallest(list_items):
    smaller = list_items[0]
    for x in list_items:
        if x < smaller:
            smaller = x
    return smaller
print(smallest([20,6,76,10]))