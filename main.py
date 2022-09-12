
import wifi_qrcode_generator as qr
def generate_qr(name, type, password):

    image = (qr.wifi_qrcode(name, False, type, password))
    image.save("code_qr.png")

if __name__ == '__main__':
    ssid= "your ssdi"
    type= "your type"
    password = "your pass"
    generate_qr(ssid, type, password)

