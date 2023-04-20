import qrcode 

#criar um código QR 
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#Adicionar dados ao QR code:
data= "https://www.google.com"
qr.add_data(data)
qr.make(fit=True)

#Criar uma imagem do código QR
img = qr.make_image(fill_collor="black", back_color="white")

#Salvar imagem e um arquivo
img.save("qr_code.png")