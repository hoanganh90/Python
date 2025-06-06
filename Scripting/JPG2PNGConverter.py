import sys
import os
from PIL import Image
# Grab the 1st and 2nd arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# Check if new folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Loop through all files in the Pokedex to convert them
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}/{filename}")
    if img.format == 'JPEG':
        # Convert the image to PNG
        png_filename = os.path.splitext(filename)[0] + '.png'
        img.save(f"{output_folder}/{png_filename}", 'PNG')
        print(f"Converted {filename} to {png_filename}")
    else:
        print(f"Skipped {filename}, not a JPEG image.")
