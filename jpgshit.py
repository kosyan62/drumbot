from PIL import Image 

filename = "1.jpg"
img = Image.open(filename) 
left = 0 
right = 555
up = 100
down = 340
im_res = img.crop((left, up, right, down))
im_res.save("resize_1.jpg")
