nums =[1,2,3,4,5,6,7,8,9]

names=['Martin','Mark','Folix','Ann','Mary']
heroes=['Batman','Spiderman','Hulk','Deadpool','Batman' ]

my_dict= {}
for names,heroes in  zip(names,heroes):
    my_dict[names]= heroes
print(my_dict)
#creating a pair of values in a dictionary using the zip method to generate alist