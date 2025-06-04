from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")
resized_img = img.resize(400,400)
print(img.size)
resized_img.show()