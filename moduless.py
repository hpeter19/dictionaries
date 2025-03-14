import examplee #name of the module. user creation

result = examplee.pi
result = examplee.square(3)
result = examplee.area(14)
result = examplee.cube(12)
result = examplee.circumfrence(14)

print (result)
#module 


pi =3.1433

def square(x):
    return x ** 2
def cube(w):
    w ** 3
def circumfrence(radius):
    return 2 * pi * radius
def area(radius):
    return pi*radius ** 2
