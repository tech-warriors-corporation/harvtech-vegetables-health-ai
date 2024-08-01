#!/bin/bash

mkdir -p constants/weights
# Tomato
wget -O constants/weights/best_tomato_leaf_inceptionV3_256.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_tomato_leaf_inceptionV3_256.h5
# Rice
wget -O constants/weights/best_rice_leaf.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5
# Bean
wget -O constants/weights/best_bean_leaf.pth https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/weights/best_bean_leaf.pth
# Potato
wget -O constants/weights/best_potato_leaf.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/weights/best_potato_leaf.h5

# List the files
ls -laR constants/weights