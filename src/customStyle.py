import PIL
from PIL import Image, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import  GappedSquareModuleDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask



if not hasattr(PIL.Image, 'Resampling'):
  PIL.Image.Resampling = PIL.Image
# Now PIL.Image.Resampling.BICUBIC is always recognized.

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

# used to convert your square logo into rounded corener logo
im = Image.open('./assets/microsoft-logo.jpg')
im = add_corners(im, 100)
im.save('./assets/microsoft-rounded-logo.png')


qr = qrcode.QRCode(version=4,
                   error_correction=qrcode.constants.ERROR_CORRECT_H)

qr.add_data('http://www.zippyout.com')


qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=GappedSquareModuleDrawer(),
                       color_mask=SolidFillColorMask(front_color=(59, 89, 152)),
                       embeded_image_path="./assets/microsoft-rounded-logo.png"
                       )

qr_img.save("output/microsoft_qr.png")