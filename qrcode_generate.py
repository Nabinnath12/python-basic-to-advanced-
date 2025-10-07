import qrcode 
print("personal qr code generator")
name = input("please enter your name:  ")
email = input("please enter your email:  ")
phone = input("please enter your phone number :  ")
website = input("please enter your website :   ")
address = input("please enter your address:")
college = input ("please enter your college name :")
nationality = input("please enter your nationality: ")
age = input("please enter your age :  ")
education =input("please enter your  education:")
hubby = input("please enter your hubby::")

data = f"""
👤Name           = {name}
📧email          = {email}
📲phone          = {phone}
🌎website        = {website}
🏠address        = {address}
🏫college        = {college}
🏞nationality    = {nationality}
🎈age            = {age}
💻📚education    = {education}
hubby            = {hubby}
"""
qr = qrcode.make(data)
file_name = f"{name.replace(' '  , '_')}_.png"
qr.save(file_name)
print("qrcode generate successfully: ")

