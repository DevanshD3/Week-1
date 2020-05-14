from matplotlib.image import imread
from matplotlib.pyplot import imshow
from PIL import Image
import numpy as np

img = imread('numpy_img.jpg')
imshow(img)
#to invert color of a pixel we subtract the pixels color values from 255
# img.shape gave us (1000,1000,3)
invert_img=255-img[:,:,:3]

invert_img= Image.fromarray(invert_img, 'RGB')
invert_img.save('test.jpg')
imshow(invert_img)