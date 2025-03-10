# args -allows you to pass multiple non -key arguments
# kwargs - allows you to pass multiple keyword -arguments
# *unpacking character
# args enables you to add multiple values
def add(*args):
        total= 0
        for arg in args:
            total+= arg
        return total    
print(add(1,4,5))

    