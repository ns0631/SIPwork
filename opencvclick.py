# import the necessary packages
import argparse
import cv2

def record_click(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, y)

image = cv2.imread('carimage.jpg')

cv2.namedWindow("image")
cv2.setMouseCallback("image", record_click)
#cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	# if the 'c' key is pressed, break from the loop
	if key == ord('q'):
		break

cv2.destroyAllWindows()