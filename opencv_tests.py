# Use opencv to process images and detect faces thanks to haarcascade
import cv2
import numpy as np
import glob 
import matplotlib.pyplot as plt

def opencvDet(img, scaleFactor=1.1, minNeighbors=5):
	# load the image with faces
	image = cv2.imread(img)

	# load the pre-trained model - Haar cascade
	classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	# Process the image to perform face detection

	bboxes = classifier.detectMultiScale(image, scaleFactor = scaleFactor, minNeighbors =minNeighbors)
	# Display bounding box for each detected face
	for box in bboxes:
		# extract
		x, y, width, height = box
		x2, y2 = x + width, y + height
		# Draw a rectangle over the image to display the face area
		cv2.rectangle(image, (x, y), (x2, y2), (0,0,255), 1)

	return image
	

#cv2.imwrite('./results/'+img[8:-4]+'_'+str(minNeighbors)_str()+'.jpg', image)

# Display the resulting image
cv2.imshow('face detection', opencvDet("./dataset/test_test2.jpg"))
cv2.imwrite("./dataset/test_test2_pred.jpg", opencvDet("./dataset/test_test2.jpg"))

# Until we press a key keep the window opened
cv2.waitKey(0)

# Close the window and return to terminal
cv2.destroyAllWindows()

# What are the parameters to improve
# What are the specifications that you can give
# Advantages and problems
w = 10
h = 10
fig = plt.figure(figsize=(8, 8))


images_list = glob.glob("dataset/*.jpg")
#print(images_list[1][8:-4])
# for image in images_list[5:6]:
# 	draw_images = []
# 	i = 0
# 	for minNeighbors in range(0, 10, 3):
# 		for scaleFactor in np.linspace(1.1, 1.4, 5):
# 			i+=1
# 			print(scaleFactor, minNeighbors, i)
# 			draw_images.append(opencvDet(image, scaleFactor, minNeighbors))
# 			fig.add_subplot(4, 5, i)
# 			plt.imshow(opencvDet(image, scaleFactor, minNeighbors))
			
# 	plt.show()