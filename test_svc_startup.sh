#!/bin/bash

# Run the main application in background ''&''
python main.py &

# Run tests
python tests/test_prediction_api.py
python tests/test_prediction_function.py
python tests/test_prediction_schema.py
