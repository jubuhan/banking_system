
initialAcNo=50000000

import json
import acststement
def update_data():
    file=open('project\\users.txt',"w")
    content=""
    for i in user_list:
        content=content+str(i)+"\n"
    file.write(content)

def Acdetails():
    print("account details\n")
    for i in user_data:
        if i=="password":
            continue
        print(i,":",user_data[i])
    
def deposite(username):
    print("deposit")
    amount=float(input("enter the amount\n"))
    for i in user_list:
        if i['user_name']==username:
            i["Ac_balance"]=i["Ac_balance"]+amount
    
    update_data()
    acststement.createEntry(username,amount,"credit")
    print("deposit succesful")

    
def withdraw(username):
    print("withdraw")
    amount=float(input("enter the amount\n"))
    if amount>user_data["Ac_balance"]:
        print("balance not enough")
        return
    for i in user_list:
        if i['user_name']==username:
            i["Ac_balance"]=i["Ac_balance"]-amount
    print("withdraw successful")
    
    update_data()
    acststement.createEntry(username,amount,"depit")
def transfer(user):
    print("trancefer")
    acNumber=int(input("enter the ac number to which want you to trancefer\n"))
    amount=float(input("enter the amount\n"))
    if amount>user_data["Ac_balance"]:
     print("balance not enough")
     return
    acExist=0
    for i in user_list:
       if i["AcNo"]==acNumber:
           acExist=1
       
    if acExist==0:
     print("this account number does not belongs to anyone\n")
     return
    for i in user_list:
        if i["user_name"]==user:
            i["Ac_balance"]=i["Ac_balance"]-amount
        if i["AcNo"]==acNumber:
            i["Ac_balance"]=i["Ac_balance"]+amount
    
    update_data()
    acststement.createEntry(user,amount,"depit")
    print("trnsfer succesful")
        

def Acstatement():
    print("account statement")
    statfile=open("project\\acstatement.txt")
    filecon=statfile.read()
    filesplt=filecon.split("\n")
    for i in filesplt:
        linesplt=i.split(" ")
        if linesplt[0]==user_name:
            print(i)
user_data={}
user_list=list()
def valid_user(username,password):
    global user_data
    global user_list
    users_data=open("project\\users.txt")
    contant=users_data.read()
    splt=contant.split("\n")
    
    
    for i in splt:
        if i=="":
            continue
        to_dq=i.replace("'","\"")
        user_list.append(json.loads(to_dq))
    userfound=0
    passwordfound=""
    for value in user_list:
        if value["user_name"]==username:
            userfound=1
            passwordfound=value["password"]
            user_data=value
    
    if userfound==0:
        print("invalid user name")
    elif userfound==1:
        if passwordfound==password:
            print("login succesfully")
            return "success"
        else:
            print("invalid password")





def getNumberOfUsers():
    users_file=open("project\\users.txt")
    contant=users_file.read()
    consplit=contant.split("\n")
    NumberOfUsers=len(consplit)
    return NumberOfUsers



def register():
    userCount=getNumberOfUsers()
    AcNo=initialAcNo+userCount
    name=input("enter your name\n")
    phno=input("enter your phone number\n")
    adress=input("enter your adress\n")
    email=input("enter your email id\n")
    user_name=input("enter a user name\n")
    password=input("enter a password\n")
    
    userData={
        "name":name,
        "phno":phno,
        "adress":adress,
        "email":email,
        "user_name":user_name,
        "password":password,
        'AcNo':AcNo,
        "Ac_balance":0
    }
    userdatastr=str(userData)
    userdatastr=userdatastr+"\n"
    users_file=open("project\\users.txt","a")
   
    users_file.write(userdatastr)
    print("registration succesful")

print("welcome to progress bank please choose one of the following option")
option=input("1.loigin\t2.register\n")
if option=="1":
    user_name=input("enter the user name\n")
    password=input("entrer the password\n")
    valid=valid_user(user_name,password)
    if valid=="success":
         print("select one of the following option\n1.view account details\n2.deposit\n3.withdraw\n4.transfer\n5.view account statement\n")
         option2=input()
         if option2=="1":
             Acdetails()
         elif option2=="2":
             deposite(user_name)
         elif option2=="3":
             withdraw(user_name)
         elif option2=="4":
             transfer(user_name)
         elif option2=="5":
             Acstatement()
         else:
             print("invali option")
         


elif option=="2":
    register()
else:
    print("invalid option")
