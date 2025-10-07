user_Name = "nabin nath"
user_password = "Ram@#$123"

username = input("please enter your user name::  ")
password =  input ("please enter your password:::  ")

if user_Name == username and  user_password == password :
    print("login successfull:: ")
elif user_Name != username and user_password == password :
    print("username doesnot match  please try again ! ")
elif user_Name == username and user_password != password :
    print("your password doesnot match  please try again !")
else:
    print("invalid your user name and password  ! ")     
    