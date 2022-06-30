import pickle
import flask
import os

app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))
model = pickle.load(open("linearmodel.pkl","rb"))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/predict', methods=['POST'])
def predict():
    features = flask.request.get_json(force=True)['features']
    prediction = model.predict([features])[0,0]
    response = {'prediction': prediction}
    return flask.jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)