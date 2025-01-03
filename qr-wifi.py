import qrcode
import qrcode.constants

from dotenv import load_dotenv
import os

load_dotenv()

data = {
    "S": os.getenv('WIFI_S'),
    "T": os.getenv('WIFI_T'),
    "P": os.getenv('WIFI_P')
}

wifi = f"WIFI:S:{data['S']};T:{data['T']};P:{data['P']};;"

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
 )

qr.add_data(wifi)
qr.make(fit = True)

img = qr.make_image(fill_color = 'black', black_color = 'white').convert('RGB')

img.save('wifi-casa.png')