student_register = {
 "nabin nath" :[80,90,70,79],
 "janak kc": [88,90,60,79],
 "rajan oli":[86,90,78,79],
 "lok bahadur khatri": [88,90,70,93],
 "shyam gc": [83,95,70,79]

}
print(". grade student report :")
for name , marks in student_register.items():
    total = sum(marks )

    average = total / len(marks)

    if average >= 90:
        grade = "A+"    
    elif average>=80 :
        grade = "A"
    elif average >= 70 :
        grade = "B+"
    elif average >= 60 :
          grade = "B"
    elif average >= 50 :
        grade = "c+"
    else:
        print("fail")

    print(f"\nname : {name}")
    print(f"marks:{marks}")
    print(f"total:{total}")
    print(f"average:{average}")
    print(f"grade:{grade}")        
            
