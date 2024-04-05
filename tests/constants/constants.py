SUCCESS_TEST_DATA = [
    {
        "model_type": "bean_leaf",
        "content_url": "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/XEdCnnb3EpmMHqvpwTfmjj-1024-80.jpg.webp"
    },
    {
        "model_type": "potato_leaf",
        "content_url": "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/potato_late-blight_08_zoom-Photo-OMAFRA-900x580.jpeg"
    },
    {
        "model_type": "tomato_leaf",
        "content_url": "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/0034a551-9512-44e5-ba6c-827f85ecc688___RS_Erly.B%209432.png"
    },
    {
        "model_type": "rice_leaf",
        "content_url": "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/brownspotDSC_0100.jpg"
    }
]

FAILURE_TEST_DATA = [
    {
        "description": "Invalid model type",
        "payload": {
            "model_type": "invalid_model",
            "content_url": "https://example.com/image.jpg"
        },
        "expected_status": 400
    },
    {
        "description": "Invalid URL",
        "payload": {
            "model_type": "bean_leaf",
            "content_url": "not_a_valid_url"
        },
        "expected_status": 400
    },
    {
        "description": "Unreachable URL",
        "payload": {
            "model_type": "bean_leaf",
            "content_url": "https://example.com/unreachable_image.jpg"
        },
        "expected_status": 400
    }
]
