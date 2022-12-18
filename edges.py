from PIL import Image, ImageFilter

before =  Image.open("highlands.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("twee.bmp")
