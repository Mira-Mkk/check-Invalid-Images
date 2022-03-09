import os
import imghdr
# the path shouldn't have a subfolder
path = "./dataset/your_folder/"
dir_ = os.listdir(path)

for image in dir_:
    file = os.path.join(path,image)
    # The assertion will fail if the path is actually of a folder not an image or a file
    assert os.path.isfile(file)
    
    # imghr is a module determines the type of image contained in a file or byte stream .
    #imghdr.what(file) function : tests the image data contained in the file named by file, and returns a string describing the image type.
    # not imghdr.what(file)=false when the type is one of those : rgb,gif,pbm,pgm,ppm,tiff,rast,xbm,jpeg,bmp,png,webp,exr
    if not imghdr.what(file):
        print(file)
        #if you want to remove them, uncomment next line
        #os.remove(file)
