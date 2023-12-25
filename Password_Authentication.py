import getpass
database = {"stone": "123456", "chimez": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")#getpass() func is used to get user pwd 2ru terminal
for i in database.keys():
    if username == i and password == database.get(i):
        print("Verified")
        break
if password != database.get(i):
    print("Wrong username or password")
    # if username == i:
    #     while password != database.get(i):# get, a dict mthd for getting a value of the given key
    #         password = getpass.getpass("Enter Your Password Again : ")
    #     break

#print("Verified")

