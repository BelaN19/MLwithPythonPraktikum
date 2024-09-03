from PIL import Image

image = Image.open("rooster.jpg")

pixels = image.load()

summe=0
counter=0
for i in range(image.width):
    for j in range(image.height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (r//2,g//2,b//2)

image.save("halfIntensity_image.jpg")
image.show()