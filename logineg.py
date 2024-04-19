'''if(5>10):
    print("yes")
else:
    print("no")
age1=int(input())
age2=int(input())
if(age1>age2):
    age3=age1+age2
    print(age3)
else:
        age3=age1-age2
        print(age3)'''
emailid='bitm@gmail.com'
psswd=123456789
otp=7841
email=str(input("enter user id"))
passd=str(input("Enter ur password"))
otp1=str(input("Enter the otp"))
if(email==emailid):
    if(passd==psswd):
        print("login success")
    else:
        print("login failed due to wrong pwd")
else:    
    print("login failed due to wrong userid ")
if(otp==otp1):
    print("Transcation successfull")
else:
    print("wrong otp")