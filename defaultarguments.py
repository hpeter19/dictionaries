#arbitrary Argument
#args in numbers
def add(*args):
    total=0
    for arg in args:
        total +=arg
    return total
print(add(122,122,133))