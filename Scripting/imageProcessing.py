from PIL import Image, ImageFilter
img = Image.open("./pikachu.jpg")
print(img)
print(img.format)
print(img.size)
print(img.mode)
filtered_img = img.filter(ImageFilter.SMOOTH_MORE)  # Apply a smoothing filter to the imag
filtered_img.save("./blurred_pikachu.png", "png")
converted_img = img.convert("L")  # Convert the image to grayscale
converted_img.save("./grayscale_pikachu.png", "png")
rotated_img =converted_img.rotate(90)  # Rotate the grayscale image by 90 degrees
rotated_img.show()  # Display the grayscale image