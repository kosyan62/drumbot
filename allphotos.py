from PIL import Image
import random

for i1 in range(1,16):
    for i2 in range(16,22):
        im1 = Image.open("cuted/firstpart/%i.jpg" % i1)
        im2 = Image.open('cuted/secondpart/%i.jpg' % i2)
        width = im2.width + im1.width
        final = Image.new(mode = "RGB", size = (width, 150), color = (255,255,255))
        bl_h1 = im1.height - 1
        width = im1.width  -3
        while (True):
            cordinates = width, bl_h1
            px = im1.getpixel(cordinates)
            bl_h1 -= 1
            if px < (30, 30, 30):
                break

        bl_h2 = im2.height - 1
        width = 3
        while (True):
            cordinates = width, bl_h2
            px = im2.getpixel(cordinates)
            bl_h2 -= 1
            if px < (30, 30, 30):
                break
        final.paste(im1, (0, bl_h2 - bl_h1))
        final.paste(im2, (im1.width, 0))
        print("Done:\nfirst - %i\n second %i\n" %(i1, i2))
        final.save("cuted/final/%s_%s.jpg" % (i1, i2))
