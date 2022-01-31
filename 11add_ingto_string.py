from audioop import add
from winreg import HKEY_LOCAL_MACHINE


def add_string(str):
    lenght = len(str)
    if lenght > 2:
        if str[-3:] == "ing":
            str += 'ly'
        else:
            str +='ing'
    else:
        print("not defined")
    return str
print(add_string("call"))
print(add_string("falling"))
print(add_string("he"))