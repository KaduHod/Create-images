import qrcode

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)

qr.add_data('meu pau na sua mao')

qr.make(fit = True)

img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('testeQr.png')