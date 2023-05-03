from flask import Flask, request, jsonify
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    Latitude = float(request.form['Latitude'])
    Longitude = float(request.form['Longitude'])
    Depth = float(request.form['Depth'])

    input_query = np.array([[Latitude, Longitude, Depth]])
    input_data = np.array(input_query, dtype=float)
    result = model.predict(input_data)

    return jsonify({'earthquake': str(result)})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
