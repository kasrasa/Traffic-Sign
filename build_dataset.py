import config
import os
import numpy as np
import cv2
import pandas as pd


num_classes = 43
training_images = []
labels = []

# read in the training images
for classes in range(num_classes):
    images_path = os.path.join(config.Train_path,str(classes))
    train_path = os.listdir(images_path)

    for images in train_path:
        image_path = os.path.join(images_path,images)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image = cv2.resize(image,(30,30))
        image = np.array(image)
        image = image/255.0
        training_images.append(image)
        labels.append(classes)

training_images = np.array(training_images)
labels = np.array(labels)

# read in the test images
test_images = []
test_labels = []
test_images_paths = os.listdir(config.Test_path)
for images in test_images_paths:
    image_path = os.path.join(config.Test_path,images)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(30,30))
    image = np.array(image)
    image = image/255.0
    test_images.append(image)

test_path = os.path.join(config.base_path,'Test.csv')
test_table = pd.read_csv(test_path)
test_images = np.array(test_images)


