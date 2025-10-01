name = (input("please enter your name ::"))

rollno =(input("please entr your rollno ::"))

english = int  (input("entetr the your english subject marks::"))
if(english < 1 or english > 100 ):
    print("invalid marks ::please enter the marks between 0 and 100 ")
    exit()

math = int (input("enter the math subject marks::"))
if(math < 1 or math > 100 ):
    print("invalid marks ::please enter the marks between 0 and 100 ")
    exit()

social = int (input("enter the social subject marks::"))
if(social < 1 or social > 100 ):
    print("invalid marks ::please enter the marks between 0 and 100 ")
    exit()


nepali = int (input("enter the nepali subject marks::"))
if(nepali < 1 or nepali > 100 ):
    print("invalid marks ::please enter the marks between 0 and 100 ")
    exit()

computer =int  (input("enter the computer subject marks::"))
if(computer < 1 or computer > 100 ):
    print("invalid marks ::please enter the marks greater then 0 and smaller the  100 ")
    exit()

total_marks =  (english + math + social + nepali + computer ) 
percentages  = total_marks/5

if(percentages >= 90 ): 
    print(F"your  grage is A+:")
elif(percentages >= 80):
    print("your grade is A::")
elif(percentages >= 70):
    print("your grade is  B+::")
elif(percentages >= 60):
    print("your grade is B::")
elif(percentages >= 50):
    print("your grade is c+::")
elif(percentages  >=  40):
    print("your grade is c::")
elif(percentages >= 30):
    print("your grade is D+:")
else: 
    print("please try again your grade is [NG:]") 
    print("your enter number is invalid ")


print(f"student name is :{name}")
print(f"student rollno is :{rollno}")
print(f"student english subject marks is :{english}")
print(f"student MATH subject MARKS is :{math}")
print(f"student social subject marks is :{social}")
print(f"student computer subject marks is :{computer}")
print(f"the student nepali subject marks is : {nepali}")

print(f"the total marks of student is ::{total_marks} ")
print(f"the total percentage of the studnet is :: {percentages}.%")




    

