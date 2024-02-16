#program using OpenCV in Python that loads an image in grayscale, displays it, save the image if you press ‘s’ and exit, or simply exit without saving if you press ESC key
#---------------------------------------

import cv2

gimg = cv2.imread("D:/colours.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow('GrayScale', gimg)

k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
  
elif k==ord('s'):
    cv2.imwrite("D:/colours_g.png",gimg)
    print('Gray Image saved')
    cv2.destroyAllWindows()
