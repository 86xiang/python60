from PIL import Image

im = Image.open('d:\\pic1.bmp')
im2 = Image.open('d:\\pic1.bmp')
size = im.size

box1 = (0, size[1] / 2, size[0] / 2, size[1])
region1 = im.crop(box1)
box2 = (0, 0, size[0] / 2, size[1] / 2)
region2 = im.crop(box2)
box3 = (size[0] / 2, 0, size[0], size[1] / 2)
region3 = im.crop(box3)
box4 = (size[0] / 2, size[1] / 2, size[0], size[1])
region4 = im.crop(box4)

im2.paste(region1, box3)
im2.paste(region3, box1)
im2.paste(region2, box4)
im2.paste(region4, box2)

im2.save('d:\\pic4.bmp')
im.close()
im2.close()
