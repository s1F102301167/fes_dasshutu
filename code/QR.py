import qrcode

# URLを指定
url = "https://s1f102301167.github.io/fes_dasshutu/code/my_page.html"

# QRコードを生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# 画像として保存
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")