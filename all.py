from PIL import Image
import random
import os
from randomrhytm import make_images
import errno

try:
    os.makedirs('tmp')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
try:
    img = Image.open('groove.jpg')
except:
    print("Fatal error\n can't open groove.jpg")
img = img.rotate(-0.5)
try:
    img.save("tmp/tmp.jpg")
except:
    print("Error\nCan't save tmp.jpg")
    exit
try:
    im = Image.open('tmp/tmp.jpg')
except:
    print("Fatal error\n Can't open tmp.jpg")
    exit

list = [215, 715, 1185]
x = 1

for width in list:
    height = 400
    while (height < 1200):
        cordinate = width, height
        try:
            px = im.getpixel(cordinate)
        except:
            print(f"Fatal error\nCan't get pixel {coordinate} from tmp.jpg")
        if (px == (0, 0, 0)):
            try:
                cr_im = im.crop((width - 15, height - 50, width + 315, height + 100))
                height = height + 60
                cr_im.save('tmp/firstpart%s.jpg' % x)
            except:
                print(f"Error\nCan't cat image {x}")
            x = x + 1
        else:
            height = height + 1



list = [213, 712, 1184]
x = 16
for width in list:
    height = 1430
    while (height < 1900):
        cordinate = width, height
        try:
            px = im.getpixel(cordinate)
        except:
            print(f"Fatal error\nCan't get pixel {coordinate} from tmp.jpg")
        if (px == (0, 0, 0)):
            try:
                cr_im = im.crop((width - 15, height - 50, width + 315, height + 100))
                height = height + 60
                cr_im.save('tmp/secondpart%s.jpg' % x)
            except:
                print(f"Error\nCan't cat image {x}")
            x = x + 1
        else:
            height = height + 1

print("Temp images done")
for i in range(1, 16):
    filename = "tmp/firstpart%s.jpg" % i
    try:
        im = Image.open(filename)
    except:
        print(f"Error\nCan't open {filename} to cut half")
    height = 30
    width = 150

    while (width < 230):
        cordinates = width, height
        try:
            px = im.getpixel(cordinates)
            if px < (50, 50, 50):
                im_cut = im.crop((0, 0, width - 20, im.height))
                im_cut.save('tmp/cutedfirstpart%s.jpg' % i)
                break
        except:
            print(f"Error\ncan't cut half image {i}")
            break
        width += 1

for i in range(16, 23):
    filename = "tmp/secondpart%s.jpg" % i
    try:
        im = Image.open(filename)
    except:
        print(f"Error\nCan't open {filename} to cut half")
    height = 30
    width = 150

    while (width < 230):
        cordinates = width, height
        try:
            px = im.getpixel(cordinates)
            if px < (50, 50, 50):
                im_cut = im.crop((width - 17, 0, im.width, im.height))
                im_cut.save('tmp/cutedsecondpart%s.jpg' % i)
                break
        except:
            print(f"Error\ncan't cut half image {i}")
            break
        width += 1
print("All images done")
make_images()
