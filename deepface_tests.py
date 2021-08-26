from deepface import DeepFace
import glob 
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

images_list = glob.glob("dataset/*")


#result  = DeepFace.verify(r"dataset\chris_hemsworth.jpg", r"dataset\test_chris.jpg")
#print("Is verified: ", result["verified"])

#df = DeepFace.find(img_path = "dataset\chris_hemsworth.jpg", db_path = "./dataset")
#print(df)

# metrics = ["cosine", "euclidean", "euclidean_l2"]
# for metric in metrics:
#    #result =DeepFace.verify(r"dataset\chris_hemsworth.jpg", r"dataset\test_chris.jpg", distance_metric = metric)
#    df = DeepFace.find(img_path = "dataset\test2.jpg", db_path = "./dataset", distance_metric = metric)

# backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']
# df = DeepFace.find(img_path = "./dataset/test1b.jpg", db_path = "./face_detection/images/") #, distance_metric = metric)
# print(df)

# li = glob.glob('./face_detection/images/*')

# print(li)
# for img in li:
#     detected_face = DeepFace.detectFace(img)
#     im = Image.fromarray((detected_face*255).astype(np.uint8))
#     im.save(img)



detected_face, a, faces = DeepFace.detectFace("./dataset/test2.jpg", detector_backend="retinaface")
# print(len(detected_face))
# print(detected_face.shape)
# print(detected_face)
# print(a)
print(faces)
print(len(faces))
print(faces[0])
for face in faces:        
    plt.imshow(face)
    plt.show()