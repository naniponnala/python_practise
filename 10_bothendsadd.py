def both_ends(string):
    if len(string) <2:
        return ''
    return string[0:2] + string[-2:]
print(both_ends('heyjaanu'))