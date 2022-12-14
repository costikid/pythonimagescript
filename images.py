# import the libraries
from PIL import Image, ImageOps
from os import listdir
from os.path import splitext, basename
#path of the folder where you want to save the images after they have been modified 
folder = "./media/"
path_list = listdir(f"./{folder}")
# Making the images a square with a minimum size of 1000x1000 and filling in a white background if needed
def make_square(im, min_size=1000, fill_color=(255,255,255, 0)):
    
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)

    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

for name in path_list:
    image = Image.open(f"./{folder}/" + name)


    new_name = splitext(basename(f"./{folder}/" + name))[0].replace(' ', '')
    
    make_square(Image.open(f"./{folder}/" + name)).save(f"./{folder}/" + name)
    
    try:
        image.save("./output/" + new_name + ".png", "PNG", optimize=True, quality=100)
    except:
        image.save("./output/" + new_name + ".png", optimize=True, quality=100)


