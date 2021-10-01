import qrcode

data = "https://google.com"

filename = "n.png"
img = qrcode.make(data)

img.save(filename)
