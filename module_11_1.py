from PIL import Image, ImageDraw, ImageFont, ImageFilter
import time

filename = "Statham.jpg"
with Image.open(filename) as img:
    img.show()
    time.sleep(2)

    print("Информация о изображении:")
    print(img.format)
    print(img.size)
    print(img.mode)

    new_size = (920, 300)
    resized_img = img.resize(new_size)
    resized_img.show()
    time.sleep(2)

    draw = ImageDraw.Draw(resized_img)
    font = ImageFont.truetype('CypressHell.ttf', 100)
    draw.text((200, 100), "PILLOW",fill='black', font=font)
    resized_img.show()
    time.sleep(2)

    font = ImageFont.truetype('CypressHell.ttf', 96)
    draw.text((205, 100), "PILLOW",fill='red', font=font)
    resized_img.show()
    time.sleep(2)

    resized_img = resized_img.filter(ImageFilter.BLUR)
    resized_img.show()
