from datetime import datetime
current_year =  datetime.now().year

birth_year = input("plese enter your english  birth year format 'YYY':  ")

age = current_year - int(birth_year)
print(f"you are {age} years old   :  ")

