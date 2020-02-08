from PIL import Image
import random
import os
import errno

def make_images():
    try:
        os.makedirs('rhytms')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for i1 in range(1,16):
        for i2 in range(16,22):
            try:
                im1 = Image.open("tmp/cutedfirstpart%i.jpg" % i1)
                im2 = Image.open('tmp/cutedsecondpart%i.jpg' % i2)
            except:
                print("Can't open Image")
            width = im2.width + im1.width
            try:
                final = Image.new(mode = "RGB", size = (width, 150), color = (255,255,255))
            except:
                print("Making new Image error")
            bl_h1 = im1.height - 1
            width = im1.width  -3
            while (True):
                cordinates = width, bl_h1
                try:
                    px = im1.getpixel(cordinates)
                except:
                    print(f"Cant get pixel from coordinates at left half\n{cordinates}")
                    break
                bl_h1 -= 1
                if px < (30, 30, 30):
                    break

            bl_h2 = im2.height - 1
            width = 3
            while (True):
                cordinates = width, bl_h2
                try:
                    px = im2.getpixel(cordinates)
                except:
                    print(f"Cant get pixel from coordinates at right half\n{cordinates}")
                    break
                bl_h2 -= 1
                if px < (30, 30, 30):
                    break
            try:
                final.paste(im1, (0, bl_h2 - bl_h1))
                final.paste(im2, (im1.width, 0))
            except:
                print( "Filling new Image errorr")
            try:
                final.save("rhytms/%s_%s.jpg" % (i1, i2))
            except:
                print("Saving error")
    print("All rhytms done")             
