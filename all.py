from PIL import Image
import random

img = Image.open('groove.jpg')
img = img.rotate(-0.5)
img.save("rotated.jpg")

im = Image.open('rotated.jpg')

list = [215, 715, 1185]
x = 1

for width in list:
    height = 400
    while (height < 1200):
        cordinate = width, height
        px = im.getpixel(cordinate)
        if (px == (0, 0, 0)):
            cr_im = im.crop((width - 15, height - 50, width + 315, height + 100))
            print("first step done with %s part" % x)
            height = height + 60
            cr_im.save('firstpart/%s.jpg' % x)
            x = x + 1
        else:
            height = height + 1



list = [213, 712, 1184]
x = 16
for width in list:
    height = 1430
    while (height < 1900):
        cordinate = width, height
        px = im.getpixel(cordinate)
        if (px == (0, 0, 0)):
            cr_im = im.crop((width - 14, height - 50, width + 315, height + 100))
            print("second step done with  %s part" % x)
            height = height + 60
            cr_im.save('secondpart/%s.jpg' % x)
            x = x + 1
        else:
            height = height + 1

print("temp photos done")
for i in range(1, 16):
    filename = "firstpart/%s.jpg" % i
    im = Image.open(filename)
    height = 30
    width = 150

    while (width < 230):
        cordinates = width, height
        px = im.getpixel(cordinates)
        if px < (50, 50, 50):
            im_cut = im.crop((0, 0, width - 15, im.height))
            im_cut.save('cuted/firstpart/%s.jpg' % i)
            print("First part of cuted photo done. number %s" % i)
            break
        width += 1

for i in range(16, 23):
    filename = "secondpart/%s.jpg" % i
    im = Image.open(filename)
    height = 30
    width = 150

    while (width < 230):
        cordinates = width, height
        px = im.getpixel(cordinates)
        if px < (50, 50, 50):
            im_cut = im.crop((width - 17, 0, im.width, im.height))
            im_cut.save('cuted/secondpart/%s.jpg' % i)
            print("Second part of cuted photo done. number %s" % i)
            break
        width += 1
