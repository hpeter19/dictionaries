
#basic user login 
username=input("Enter your names:")


if len(username) > 12:
    print("username must be less than 12 characters")
elif not username.find(" ") == -1:
    print("username cannot contain spaces")
elif not username.isalpha():
    print("username cannot contain digits")       
else:
    print(f"welcome{username}")    