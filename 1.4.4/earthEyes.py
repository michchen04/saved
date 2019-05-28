'''
earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 

13. matplotlib.pyplot (plt) – It allows interactive plot charts to be used
    numpy (np) – It allows use to have tools and math capabilities 
    PIL – Allows us to manage image files
15a.  Line 19 calls the function subplots() from the matplotlib.pyplot library. 
The function is being called with 2 argument(s): 1 and 2. The function returns 1
object(s), which is/are being assigned to fig, ax.
15b. Line 20 calls __imshow()_ on ___ax[0]____
    Line 23 calls imshow() on ax[1]
    Line 24 calls set_xticks on ax[1]
    Line 25 calls set_xlim on ax[1]
    Line 26 calls set_ylim on ax[1]
    Line 27 calls save.fig on fig
15c. The XY coordinates of the corner are (1073, 879)
16. X limits: 670 - 790 ; Range: 120
    Y Limits: 960 - 1100; Range: 140
17.
A. Line 30 uses the join() method from the os.path module. It is being passed 
2 arguments. The value it returns is being assigned to the variable earth_file.

B. In line 31 the open() function of the PIL.Image module returns a new PIL.
Image object, which is being assigned to the variable earth_image. 

C. The tuple is inside of the method

D. The center of the girl's eyes

E. Line 34 calls the function imshow from the plt library with 1 
argument(s): earth_img. The function returns 1 object(s), 
which is/are being assigned to axes2[0].
f. It can take an image or a file
g. The height and the width
h. It will print two width and height and then one height
i. It is more blurry

18. I think the resize basically takes the pixels and multiplies them while
applying color to them.

19a. 
student_img bytes = 30,972
earth_small bytes = 15,667,200
d. The discrepency in the two answer is caused because of how it is saved and
how it it was resized.
e. If the color is used at the first argument, it changes the color of
the image. 
f. It changes the modes and makes it so that it changes based on that mode.
g. The purpose of the paste command is to paste the earths onto the girl's 
eyes. 


'''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('earth_small.png')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')