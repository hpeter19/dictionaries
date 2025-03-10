# args -allows you to pass multiple non -key arguments
# kwargs - allows you to pass multiple keyword -arguments
# *unpacking character
# args in accepting multiple names
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.","Jake ","Paul")


