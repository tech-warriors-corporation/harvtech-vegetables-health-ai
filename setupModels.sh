#!/bin/bash

# Download other files
curl -0 constants/weights/best_tomato_leaf_inceptionV3_256.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_tomato_leaf_inceptionV3_256.h5
curl -0 constants/weights/best_rice_leaf.h5 https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5

# List the files
ls -laR constants/weights