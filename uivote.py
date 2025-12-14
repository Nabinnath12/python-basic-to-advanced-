def vote(age):
    if age>=18:
        print("your are eligible for vote :")
    else:
        print("your are not eligible for vote ")    


user_input = int (input("plese enter your age "))  
vote(user_input)      
