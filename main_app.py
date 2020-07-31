from flask import Flask,request,jsonify
from PIL import Image
import io
from processing import data_prep,call_model
import numpy as np

app = Flask(__name__)

@app.route("/predict",methods=['POST'])

def predict():
    
    data = {'success':False}

    if request.method == "POST":
        if request.files.get('image'):

            image = request.files.get("image").read()
            image = Image.open(io.BytesIO(image))
            image = data_prep(image)

            y_pred = model.predict(image)
            y_pred = np.argmax(y_pred)
            y_pred = str(y_pred)

            data['pred'] = y_pred
            data['success'] = True

            return jsonify(data)


if __name__ == "__main__":
    model = call_model()
    app.run(debug=True)

