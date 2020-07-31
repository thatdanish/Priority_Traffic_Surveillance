import requests

url = 'http://127.0.0.1:5000/predict'
image_path = "specimens/img.jfif"
image = open(image_path,'rb').read()

payload = {'image':image}

r = requests.post(url,files=payload).json()

if r['success']:
    print(r['pred'][0])

else:
    print("POST Request Failed, check server and try again")