#program using OpenCV in Python that displays an image then waits from the keyboard interrupt. 
#If the user presses ‘c’ key, then it will save the color image in our disk
#If the user hits ‘g’ key then it saves the image in grayscale.
#----------------------------------------------

import cv2

cimg = cv2.imread("D:/colours.png",cv2.IMREAD_COLOR)
gimg = cv2.imread("D:/colours.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow('Colours', cimg)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()

elif k==ord('g'):
    cv2.imwrite("D:/colours_g.png",gimg)
    print('Gray Image saved')
    cv2.destroyAllWindows()
    
elif k==ord('c'):
    cv2.imwrite("D:/colours_c.png",cimg)
    print('Color Image saved')
    cv2.destroyAllWindows()
