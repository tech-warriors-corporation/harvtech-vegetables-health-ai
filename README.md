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
CLOUD_STORAGE_URL_PREFIX=https://URL_TO_YOUR_STORAGE_DOMAIN/
FLASK_PORT=5001
GEMINI_API_KEY=YOUR_API_KEY_HERE
FLASK_ENV=production
```

## Prepare
Download the [best_tomato_leaf_inceptionV3_256.h5](https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_tomato_leaf_inceptionV3_256.h5) and [best_rice_leaf.h5](https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5),  into the _constants/weights_ directory.

## Install and download models
Use `pip install -U -r requirements.txt` to install dependencies.

Use `./download_models.sh` to download the trained models

## Install certificates
If want to use self-certificates, run the next script to build them.

Run `./generate_certificates.sh` 

> NOTE: In production the cloud provider would set these on your behalf enabling HTTPS

## Start
Run `python3 app.py` to start project.

The `https://API_URL:PORT/predict` should be used for the POST API calls

Following an example of the API body request

```
{
    "model_type": "rice_leaf",
    "content_url": "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/brownspotDSC_0100.jpg"
}
```

## Tests
Run the directory _tests_, if in [PyCharm](https://www.jetbrains.com/pycharm) .it will execute all files with application running.
Running in CLi, run the `pytest`command on the project directory.
> NOTE: Ensure to set the `PYTHONPATH` first to make pytest localize the `app`. In Linux OS try:  `export PYTHONPATH=.`

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
