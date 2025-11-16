import segno

qrcode = segno.make_qr(input("Enter data for QR code: "))
qrcode.save("qrcode.png", scale=10)