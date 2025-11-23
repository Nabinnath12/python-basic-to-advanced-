principles = float (input("Enter your principles:: "))


time       = float (input("Enter your time:: "))

rate       = float (input("Enter your rate :: "))

a = principles * (1 + rate/100) ** time


simple_intersts = a + principles 

print(f"the compound interest is ::  {a:.2f}")

print(f"total compound  interest is ::{simple_intersts:.2f}")


