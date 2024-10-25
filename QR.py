!pip install qrcode

import qrcode as qc
image= qc.make("www.google.com")
image.save("google.png")
