import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=8,
    border=1,
)

qr.add_data('tel:12345678')

img = qr.make_image(fill_color="black", back_color="white")
img.save("output/tel.png")