import qrcode

img = qrcode.make("https://fredson.netlify.app/")
img.save("./Images/Portfolio.jpg")

img = qrcode.make('''
                  Elected current head of the state.
                  (The President) - Gisa Kaze Fredson
                  ''')

img.save("./Images/President.jpg")