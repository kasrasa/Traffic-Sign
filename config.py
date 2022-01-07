import os

# base path that we will build for each type of data
base_path = "archive_2"

# path to each forlder
Train_path = os.path.sep.join([base_path,"train"])
Test_path = os.path.sep.join([base_path,"test"])

# train, test, validation split ratio
Train_split = 0.8
Val_split = 0.1
