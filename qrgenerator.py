import qrcode
import uuid
#datos a codificar
web=input("introduzca el enlace de su pagina web: ")
#Generar un UUID
codigo_unico=uuid.uuid4()
#crear el generador de codigo QR
qr=qrcode.QRCode(   version=1,   error_correction=qrcode.constants.ERROR_CORRECT_L,   box_size=10, border=4,)
#Agregar el UUID al codigo QR
qr.add_data(web)
qr.make(fit=True)
#crear la imagen del codugo QR
img=qr.make_image(fill='black',    back_color='white')
#guardar la imagen con un nombre unico
img.save(f"codigo_qr{codigo_unico}.png")
