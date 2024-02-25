# Vegetables Health
The AI project to assess the vegetables health.

## Support vegetables:
- Bean;
- Potato;
- Tomato.

## About models
We are using models from [Kaggle](https://www.kaggle.com).

## Prepare
Download the [best_tomato_leaf_inceptionV3_256.h5](https://cdn.discordapp.com/attachments/1073387782757695539/1210385802207432785/best_tomato_leaf_inceptionV3_256.h5?ex=65ea5e9f&is=65d7e99f&hm=e428e43e4d621f0de308f2d7d3e248884494d70025ff8d2a2bbcb924cdf0c7a6&) and put this in _constants/weights_ directory.

## Install
Use `pip install -r requirements.txt` to install dependencies.

## Start
Run `python -m main` to start project.

## Tests
Run the directory _tests_ and the [PyCharm](https://www.jetbrains.com/pycharm) will execute all files.

## Roadmap:
- [X] Unit tests;
- [X] Create a REST API to use this code;
- [X] Kaggle explains;
- [X] Tests describe how to execute;
- [ ] Deploy project in VPS;
- [ ] Validation URL from back-end with prefix in DNS;
- [ ] ChatGPT return with data structured;
- [ ] Create all tests with different models;
- [ ] Search new tomato models in [Kaggle](https://www.kaggle.com);
- [ ] Integrated responses with [ChatGPT](https://chat.openai.com);
- [ ] Upload vegetable images in [cloud (Jorge)](https://cloud.ibm.com);
- [ ] Configure CORS.
