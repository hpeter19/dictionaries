nums =[1,2,3,4,5,6,7,8,9]

names=['Martin','Mark','Folix','Ann','Mary']
heroes=['Batman','Spiderman','Hulk','Deadpool','Batman' ]

my_dict= {name:hero for name ,hero in zip(names,heroes) if name !='Mark' }

print(my_dict)
#using compression to form a list from two lists of data