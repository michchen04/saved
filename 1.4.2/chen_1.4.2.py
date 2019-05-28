'''4. C:/Users/Student Login/Desktop/nice.jpg
5. Admin../Users/Student Login/Desktop/nice.jpg
6. It is an absolute filename because there is no up type of commands and it 
   starts from general to specific. The difference is where the file is coming
   from.
7. It fixed the code with the use AGG and the savefig at the bottom. 
7a. The woman's nose is at (300,400)
7b. The cat's nose is at (60,40)
8a. fig is an instance of the class Figure
	ax is an instance of the class AxesSubplot
8b. In line 25, savefig is a method that is being called to the object
fig. It has one argument. That method is a method of
the class fig.
8c. Every comment above a method call explans the reason for the call below.
9a. Savefig is being used on Fig
10. The code uses the interpolation arguement to override. Then the data points
set the limit of the x and the y to make a cut out of only the earings
12. One of the arguments is the y and x limit and the  default value is just
the whole length of the image
Conclusion: Absolute filenames start with the top while relative filename starts from wherever you want it to.
An instance of a class
Method= Function of a class     Properties: Attributes of the class
It will run the method like the code that changes it onto the object


'''



'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'mice.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
x = 38
y = 48
ax[0].plot(x, y, 'ro')
x = 117
y = 41
ax[0].plot(x, y, 'ro')
x = 138
y = 42
ax[0].plot(x, y, 'ro')
ax[0].imshow(img)
ax[1].imshow(img)
fig.savefig('crazy_mice')

# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice.png')
