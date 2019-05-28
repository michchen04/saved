import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import os.path
import PIL

directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'women.jpg')
img = plt.imread(filename)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, interpolation='none')

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

def make_mask(rows, columns, stripe_width):
    
    imga = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(imga)
    for row in range(rows):
        for column in range(columns):
            if column/stripe_width % 2 == 0: 
                image[row][column] = [155, 75, 165, 255] # pale red, alpha=0
                
            elif row/stripe_width % 2 == 0: 
                image[row][column] = [0, 255, 0, 255] # pale red, alpha=0
                
            elif (row+column)/stripe_width % 2 == 0: 
                image[row][column] = [200, 0, 0, 255] # pale red, alpha=0
            
            elif (row+column)/stripe_width % 2 == 1: 
                image[row][column] = [0, 0, 200, 255] # pale red, alpha=0
            
            else:
                image[row][column] = [255, 0, 255, 0] # magenta, alpha=255
    return image
    
image = make_mask(110,110,10)

ax[1].imshow(image)


fig.savefig('women_and_mask.png')  

              
