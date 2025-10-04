print("---welcome to  the our table  finding application---- \n")
first_number = int (input("please enter the first number :  "))
second_number = int(input("please enter the second numbe ::"))

print(f"multiplication table {first_number} to {second_number} \n ")

#for loop used 
for i in range (first_number, second_number +1):
    print("\n")
    print(f"table of {i}  \n  ")

    for j in range(1,11):
        print(f" {i} x {j} =  {i  *  j}  ")

