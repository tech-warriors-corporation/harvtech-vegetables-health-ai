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
flask_port=5000
gemini_api_key=YOUR_API_KEY_HERE
```

## Prepare
Download the [best_tomato_leaf_inceptionV3_256.h5](https://cdn.discordapp.com/attachments/1073387782757695539/1210385802207432785/best_tomato_leaf_inceptionV3_256.h5?ex=65ea5e9f&is=65d7e99f&hm=e428e43e4d621f0de308f2d7d3e248884494d70025ff8d2a2bbcb924cdf0c7a6&) and [best_rice_leaf.h5](https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/best_rice_leaf.h5), put their in _constants/weights_ directory.

## Install
Use `pip install -r requirements.txt` to install dependencies.

## Start
Run `python -m main` to start project.

## Tests
Run the directory _tests_ and the [PyCharm](https://www.jetbrains.com/pycharm) will execute all files with application running.

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
