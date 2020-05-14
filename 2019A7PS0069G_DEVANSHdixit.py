# Imports PIL module  
from PIL import Image 
import numpy as np

#printing of the numpy arrays wasn't necessary so I commented it out

# this opens the given image
im = Image.open(r"C:\Users\Dell\Desktop\kratos.jpg")  
  
# This method will show the original image in any image viewer  
im.show()  

# this converts the image into a numpy array
im = np.array(Image.open(r'C:\Users\Dell\Desktop\kratos.jpg'))
# print(im)

im=255-im #converted the numpy array into its contrast by subtracting from 255.
# print(im)

# saving and displaying its invert
in_im=Image.fromarray(im).save(r'C:\Users\Dell\Desktop\in_kratos.jpg')

#in_im has a type of "none" so we need to convert it, so that show() can be a valid function on the image
in_im=Image.open(r'C:\Users\Dell\Desktop\in_kratos.jpg')
in_im.show()

#converting it to grey-scale
im = np.array(Image.open(r'C:\Users\Dell\Desktop\kratos.jpg').convert('L')) 
# print(im) 

# saving and showing the grey scale image 
gr_im= Image.fromarray(im).save(r'C:\Users\Dell\Desktop\gr_kratos.jpg')
gr_im= Image.open(r'C:\Users\Dell\Desktop\gr_kratos.jpg')
gr_im.show()