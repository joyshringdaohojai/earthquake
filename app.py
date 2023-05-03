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
    a = model.predict(input_data)[0]

    if (a < 4):
        result = "No"
    elif (4 <= a < 6):
        result = "Low"
    elif (6 <= a < 8):
        result = "Moderate"
    elif (8 <= a < 9):
        result = "High"
    elif (a >= 9):
        result = "VeryHigh"
    else:
        result = "Undefined"

    return jsonify({'earthquake': str(result)})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

