from sklearn.externals import joblib
from flask import Flask, request, jsonify
import traceback
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    lr = joblib.load("model.pkl")  # Load "model.pkl"
    model_columns = joblib.load("model_columns.pkl")  # Load "model_columns.pkl"
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return 'No model here to use'


@app.route('/')
def hello_world():
    return 'Hallo Welt! Dieses Projekt bietet eine Flask API mit Anbindung an ein Machine Learning Modell und anschließendem Docker Deployment.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
