from PIL import Image
import numpy

ASCII = '@%#*+=-:. '
def create_pixel_info(im):
    pixels_info = []
    for i in range(im.size[1]):
        row = []
        for j in range(im.size[0]):
            row.append(rgb_im.getpixel((j, i)))
        pixels_info.append(row)
    return pixels_info

def convert_pixel_to_single(pixels_info):
    new_pixels = []
    for pixel_row in pixels_info:
        row = []
        for pixel in pixel_row:
            pixel = 0.21*pixel[0] + 0.72*pixel[1] + 0.07*pixel[2]
            #pixel = (pixel[0] +pixel[1] + pixel[2])/3
            row.append(round(pixel))
        new_pixels.append(row)
    return new_pixels

def convert_single_to_ascii(pixels):
    new_pixels = []
    for i in pixels:
        row = []
        for j in i:
            #ascii_val = int(j/3.642857142857143)-1
            ascii_val = int(j/(255/len(ASCII)))-1
            if ascii_val<0:
                ascii_val=0
            row.append(2*ASCII[ascii_val])
        new_pixels.append(row)
    return new_pixels


im = Image.open("2bAvatar.png")
rgb_im = im.convert('RGB')
pixels_info = convert_pixel_to_single(create_pixel_info(im))
image = convert_single_to_ascii(pixels_info)

f = open(im.filename[:-4]+".txt", "w")
for i in image:
    line = ''.join(i)
    f.write(line+'\n')
    
f.close()