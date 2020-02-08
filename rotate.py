from PIL import Image

def rotate():

    img = Image.open('groove.jpg')
    img = img.rotate(-0.5)
    img.save("rotated.jpg")
