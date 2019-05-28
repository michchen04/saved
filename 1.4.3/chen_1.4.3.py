from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''
5) the image height = the number of rows of pixels = print(len(img[0]))
	the image width = the number of columns = print(len(img))
	the green intensity at (5,9) = img[5][9][1]
    the red intensity at (4,10) = [4][10][0]
	the red intensity of the 25th pixel in the 50th row = [24][49][0]
7) It basically checks all the pixels by using for loops for the width and the
height. It checks how bright the pixel is by comparing it to see if it is higher
then a certain value, then it changes the pixel to a certain color.

'''

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'women.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure

'''
height = len(img)
width = len(img[0])
for row in range(285, 325):
    for column in range(90, 115):
        img[row][column] = [0, 255, 0] # red + green = yellow
'''


'''
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
            
for r in range(420, 480):
    for c in range(120, 160):
            if sum(img[r][c])> 500: 
                img[r][c]=[0,0,255] 
'''
    

fig.savefig('women_sky_earing.png')

'''
print(type(img))
print(img)
print(len(img))
print(len(img[0]))
'''

