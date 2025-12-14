def additon(a,b):

    return a+b

def subtract(a,b):

    return a-b

def multiplication(a,b):

    return a*b

def divide(a,b):

    if b== 0 :

        print("can not divide by zero :")   
    else:
        return a/b
while True:
    print("\n welcome to our calculator::")     
    print("1. Addition ")
    print("2. subtract ")   
    print("3. multiplication ")
    print("4. divide")
    print("5. exit")

    choice = input("please enter your choice 1,2,3,4,5 ::" )
    if choice == 5:
        print("good bye ")

    if choice not in ["1","2","3","4","5" ]:
        print("invalid choose:")  

        continue 

    first_number = float (input("plese enter the first number  :"))   

    second_number = float(input("please enter the second number : "))    

    if choice == "1":
        print(f"the addition of two number is ",additon(first_number,second_number))
    elif choice == "2":
        print(f"the subtract of two numbe is ",subtract(first_number,second_number))
    elif choice == "3":
        print(f"the multiplication of the two number is ", multiplication(first_number, second_number))
    elif choice == "4":
        print(f"the divide of two number is ", divide(first_number,second_number))
    
            


 

