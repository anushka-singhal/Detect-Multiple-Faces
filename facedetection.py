#Detect multiple faces
# from mtcnn import MTCNN
# import cv2

# detector=MTCNN()
# #Task1: to detect single face
# img=cv2.imread('//home/anushka/Documents/facedetection/MTCNNImage2.jpeg')
# img=cv2.resize(img,(500,500))
# output=detector.detect_faces(img)
# print(output)

# for i in output:
# 	x,y,Width,height=i['box']
# 	# Blue color in BGR
# 	color = (255, 0, 0)
# 	# Line thickness of 2 px
# 	thickness = 2
#   	# Using cv2.rectangle() method
# 	# Draw a rectangle with blue line borders of thickness of 2 px
# 	image = cv2.rectangle(img,(x,y), (x+Width,y+height), color, thickness)
# cv2.imshow('detection_image',image)
# cv2.waitKey(0)
