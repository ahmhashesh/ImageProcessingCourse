#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('jupyter nbconvert --to=python Image_Processing.ipynb')


# In[2]:


import cv2


# In[3]:


img = cv2.imread("Lenna.png",0)


# In[4]:


print (img)


# In[5]:


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# the imshow() display an image in a window. The window will be the same as the image size.
# the first argument is the image name to display and the second is the image variable.
# the Output will be like this:
# <img src="Capture.png">

# cv2.waitKey(): Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event.
# 
# zero as argument means to wait indefinitely.
# 
# cv2.destroyAllWindows() simply destroys all the windows we created. 

# In[6]:


cv2.imwrite('lenna_gray.png',img)


# In[7]:


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Lenna.png',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


# In[8]:


print(img.shape)
plt.hist(img)


# In[ ]:




