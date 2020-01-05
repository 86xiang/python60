from PIL import Image

im1 = Image.open('d:\\pic1.bmp')
im2 = Image.open('d:\\pic2.bmp')
size = im1.size

for i in range(size[0]):
    for j in range(size[1]):
        color1 = im1.getpixel((i, j))
        color2 = im2.getpixel((i, j))
        r = (color1[0] + color2[0]) // 2
        g = (color1[1] + color2[1]) // 2
        b = (color1[2] + color2[2]) // 2
        im1.putpixel((i, j), (r, g, b))

im1.save('d:\\pic3.bmp')
im1.close()
im2.close()
