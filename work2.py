from PIL import Image

for i in range(1, 16):
    filename = "firstpart/%s.jpg" % i
    im = Image.open(filename)
    height = 20
    width = 150

    while (width < 230):
        cordinates = width, height
        px = im.getpixel(cordinates)
        if px < (50, 50, 50):
            im_cut = im.crop((0, 0, width - 15, im.height))
            im_cut.save('cuted/firstpart/%s.jpg' % i)
            break
        width += 1

for i in range(16, 23):
    filename = "secondpart/%s.jpg" % i
    im = Image.open(filename)
    height = 20
    width = 150

    while (width < 230):
        cordinates = width, height
        px = im.getpixel(cordinates)
        if px < (50, 50, 50):
            im_cut = im.crop((width - 17, 0, im.width, im.height))
            im_cut.save('cuted/secondpart/%s.jpg' % i)
            break
        width += 1
