full_name =  (input ("please enter your name :  "))

email =  input("Please enter your email: ")

while True:

    phone = input("Please enter your phone number: ")

    if phone.isdigit() and len(phone) == 10:
            
            break
    else:
             print("❌ Invalid phone number, must be 10 digits.")

while True:
    address = input("Please enter your address: ")

    if address:
            break
    else:
            print("❌ Address cannot be empty!❌")

while True:
    father_name = input ("please enter your father name:    ")
    if father_name:
            break
    else:
            print("❌ father name  cannot be empty!")

while True:
    mother_name = input ("please  enter your mother name :   ")
    if mother_name:
            break
    else:
            print("❌ mother name cannot be empty!")

while True:

    nationality = input ("please enter your nationality:   ").strip()
    if nationality:
            break
    else:
            print("❌ nationality cannot be empty!")

Date_of_Birth = input ("please enter your date of birth:  ")

while True:

    faculty  = input ("please enter your faculty: ").strip()
    if faculty:
                break
    else:
            print("❌ facluty  cannot be empty!")
while True :

    password = input ("please enter your password :  ")
    confirm_password = input ("Re-enter your password ")

    if password == confirm_password:

        print(" Registration sucessful ☑️") 
        break

    else:

        print("password doesnot match ! please try againg ✕") 

#stored the data into dictionary

user_data = {
    "full_name" : full_name ,
    "email" :  email,
    "phone" : address,
    "father_name"  : father_name ,
    "mother_name " : mother_name,
    "nationality"  : nationality ,
    "Date_of_Birth" : Date_of_Birth ,
    "faculty" : faculty,
    "password" : password 

}  

#this  login section of the registration..

print("welcome to the login page \n")

user_email = input("please enter your email:  ")

user_password = input("please enter your password:   ")

if user_email == user_data["email"] and  user_password == user_data["password"]:

    print("login successful ❤️‍🔥🎉")
    print(f"welcome {user_data['full_name']} 🎉🎈")

else:
    print("❌ invalid your user name  and password !  please register the form first then the login :")    



