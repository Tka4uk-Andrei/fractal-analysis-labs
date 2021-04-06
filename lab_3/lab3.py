import cv2


img_path = 'img1.jpg'
grey_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("grey_"   + img_path, grey_img)