from PIL import Image, ImageFilter

before= Image.open("highlands.bmp")
after = before.filter(ImageFilter.BoxBlur(20))
after.save("out.bmp")
