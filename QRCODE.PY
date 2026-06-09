#QR CODE 
import qrcode

# 1. Define the data you want to embed (link or text)
data = "https://www.youtube.com/watch?v=xsUBvZbuXvU"

# 2. Create the QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 3. Add data and compile
qr.add_data(data)
qr.make(fit=True)

# 4. Generate and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("QR code generated and saved as 'my_qrcode.png'!")
