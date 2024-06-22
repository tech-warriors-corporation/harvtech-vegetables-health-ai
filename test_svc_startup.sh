#!/bin/bash

# Run the main application in background ''&''
python app.py &

# Run tests
python tests/test_prediction_api.py
python tests/tests/test_prediction_function.py
python tests/tests/test_prediction_schema.py
