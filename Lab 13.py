#Lab 13
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 26, 2020
#This program puts a green filter on an image

inMess = input('Enter name of the input file: ')
outMess = input('Enter name of the output file: ')
import matplotlib.pyplot as plt
import numpy as np
img = plt.imread(inMess)
img2 = img.copy()
img2[:,:,0] = 0
img2[:,:,2] = 0
plt.imsave(outMess, img2)