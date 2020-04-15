# program to display loggin successfull if valid credentials are entered.
#untill valid cred are entered the console request to enter cred.

Username=''
password=''

while Username !='kiran' and password !='enter':
    Username = input("Enter the Username")
    password = input("Enter the password")

else:
    print("login successful")

