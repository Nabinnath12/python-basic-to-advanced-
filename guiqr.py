import qrcode

print("Personal QR Code Generator")

name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")
image_link = input("Enter the link to your image (e.g. https://example.com/me.jpg): ")

data = f"""
👤 Name: {name}
📧 Email: {email}
📞 Phone: {phone}
🏠 Address: {address}
🖼️ Image: {image_link}
"""

qr = qrcode.make(data)
file_name = f"{name.replace(' ', '_')}_with_image_link.png"
qr.save(file_name)

print(f"✅ QR code generated with image link: {file_name}")
