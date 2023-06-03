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
        result = "No Future Earthquake Detected"
    elif (4 <= a < 6):
        result = "Minor Earthquake Detected"
    elif (6 <= a < 8):
        result = "Earthquake detected of Moderate magnitude"
    elif (8 <= a < 9):
        result = "Earthquake detected of Strong magnitude"
    elif (a >= 9):
        result = "Earthquake detected of very strong Magnitude "
    else:
        result = "Undefined"
    return jsonify({'earthquake': str(result)})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
