# generate_qr.py
import qrcode

# Your GitHub repository URL
url = "https://github.com/kjc47/HW1"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('github_repo_qr.png')
