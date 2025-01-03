import qrcode
import qrcode.constants

data = {
    "S": 'DIGIFIBRA-PLUS-D130',
    "T": 'WPA2',
    "P": 'NFL377UERG'
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