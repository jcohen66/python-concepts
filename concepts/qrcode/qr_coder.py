# Generate and Decode QrCode
# pip install qrcode
# pip install qrtools
# pip install Pillow
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
def generate_qrcode(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save("qrcode.png")
    
def Decode_Qrcode(file_name):
    result = decode(Image.open(file_name))
    print("Data:", result[0][0].decode())
    
generate_qrcode("This is Medium Article By Haider")
Decode_Qrcode("qrcode.png")