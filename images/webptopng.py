from PIL import Image

# List of your webp image filenames
webp_images = ['cancer.webp', 'data_detective.webp', 'gmail.webp', 'liverpool.webp', 'netflix.webp', 'tesla.webp']

# Loop to convert each image to PNG
for image_file in webp_images:
    img = Image.open(image_file)
    img.save(image_file.replace('.webp', '.png'), 'PNG')

print("Conversion complete.")
