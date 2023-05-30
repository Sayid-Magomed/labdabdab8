from PIL import Image, ImageDraw, ImageFont
filename = "a.jpg"
with Image.open(filename) as img:
    img.load()

cropped_img = img.crop((0, 0, 900, 600))

cropped_img.save("cropped_a.jpg")