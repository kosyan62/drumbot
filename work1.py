from PIL import Image

def make_temp_photos():
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
                print("good shit %s" % x)
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
                print("good shit %s" % x)
                height = height + 60
                cr_im.save('secondpart/%s.jpg' % x)
                x = x + 1
            else:
                height = height + 1
