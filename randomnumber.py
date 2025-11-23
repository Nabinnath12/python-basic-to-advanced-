
import  random 

capital_number = "ABCDDJJDFHHJHGGR"

small_number = "sajhdksahjfhd"

random_password = capital_number + small_number 

otp_generator = ''.join(random.choices(random_password , k=9))


print(f"your random number is the:{otp_generator}")
