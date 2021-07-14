# From line 2 to 11 it deals with creating/generating qrcode in form image
import qrcode
img = qrcode.make("https://fredson.netlify.app/")
img.save("./Images/Portfolio.jpg")

img = qrcode.make('''
                  Elected current head of the state.
                  (The President) - Gisa Kaze Fredson
                  ''')

img.save("./Images/President.jpg")
# End generating Qrcodes in form of image

# From line 15 to 19 it deals with reading qrcode from images and printing them
import cv2

detect = cv2.QRCodeDetector()
val, points, straight_qrcode =   detect.detectAndDecode(cv2.imread("./Images/Portfolio.jpg"))
print(val)
# End reading Qrcodes in form of image