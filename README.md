# Vegetables Health
The AI project to assess the vegetables health.

## Support vegetables:
- Bean;
- Potato;
- Tomato;
- Rice.

## About models
We are using models from [Kaggle](https://www.kaggle.com).

## Gemini API
You can get a Gemini API key in this [link](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br).

## Environment setup
Create a `.env` file in the root folder with content:
```
cloud_storage_url_prefix=https://URL_TO_YOUR_STORAGE_DOMAIN/
flask_port=5001
gemini_api_key=YOUR_API_KEY_HERE
```

## Prepare
Download the [best_tomato_leaf_inceptionV3_256.h5](https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_tomato_leaf_inceptionV3_256.h5) and [best_rice_leaf.h5](https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5), put their in _constants/weights_ directory.

## Install and download models
Use `pip install -U -r requirements.txt` to install dependencies.

Use `./download_models.sh` to download the trained models

## Install certificates
If in development use self-signed certificates, in production follow the steps of your SSL authorizer

### Development
Run `./generate_certificates.sh` 

## Start
Run `python3 app.py` to start project.

The `https://API_URL:PORT/predict` should be used for the POST API calls

Following an example of the API body request

```
{
    "model_type": "tomato_leaf",
    "content_url": "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/0034a551-9512-44e5-ba6c-827f85ecc688___RS_Erly.B%209432.png"
}
```

## Tests
Run the directory _tests_, if in [PyCharm](https://www.jetbrains.com/pycharm) .it will execute all files with application running.

## Roadmap:
- [X] Unit tests;
- [X] Create a REST API to use this code;
- [X] Kaggle explains;
- [X] Tests describe how to execute;
- [ ] Deploy project in VPS;
- [ ] Validation URL from back-end with prefix in DNS of [cloud (Jorge)](https://cloud.ibm.com);
- [ ] ChatGPT return with data structured;
- [ ] Create all tests with different models;
- [ ] Search new tomato models in [Kaggle](https://www.kaggle.com);
- [ ] Integrated responses with [ChatGPT](https://chat.openai.com);
- [ ] Upload vegetable images in [cloud (Jorge)](https://cloud.ibm.com);
- [ ] Configure CORS.
