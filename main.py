from PIL import Image

# Open the monochrome bitmap image
image = Image.open("1.bmp")

# Get image dimensions
width, height = image.size

# Create an empty list to store binary data
binary_data = []

# Iterate over each pixel
for y in range(height):
    for x in range(width):
        # Get the color value of the pixel (0 for black, 255 for white)
        pixel = image.getpixel((x, y))
        # Convert color value to binary (0 for black, 1 for white)
        binary_value = 0 if pixel == 0 else 1
        # Append binary value to the list
        binary_data.append(binary_value)

# Now, binary_data contains the binary representation of the image