import json
import requests

url = 'http://localhost:5000/predict'
model_type = 'potato_leaf'
image_url = "https://techwarriors-objectstorage-test.s3.us-south.cloud-object-storage.appdomain.cloud/potato_late-blight_08_zoom-Photo-OMAFRA-900x580.jpeg"

if __name__ == '__main__':
    response = requests.post(url=url, json={'content_url': image_url, 'model_type': model_type})
    if response.status_code == 200:
        json_string = response.content.decode('utf-8')
        data_dict = json.loads(json_string)
        print(data_dict['generated_text'])
    else:
        print(response.content)
        print(response.status_code)
