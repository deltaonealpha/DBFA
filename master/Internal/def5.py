import pyqrcode, png, os
from pyqrcode import QRCode 

upid = '9810141714@upi'
name = 'KPBalaji'

s = "upi://pay?pa="+'%s'%upid+"&pn="+'%s'%name+"&cu=INR"
  
# Generate QR code 
url = pyqrcode.create(s) 

url.png('payqr.png', scale = 6) 
from PIL import Image, ImageDraw, ImageFont
image = Image.open('payqr.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(r'C:\Users\balaj\AppData\Local\Microsoft\Windows\Fonts\MiLanProVF.ttf', size=200)
(x, y) = (5, 280)
xname = 'Scan to pay with UPI                  deltaDBFA'
draw.text((x, y), xname) #, fill=color)
(x, y) = (5, 5)

name = "Paying "+'%s'%name+" "*(32-len(str(name)))+"deltaPay"
draw.text((x, y), name) #, fill=color)
image.save('payqr.png', optimize=True, quality=120)

os.system(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\payqr.png')



print("deltcheCKpT")