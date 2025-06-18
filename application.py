from flask import Flask, render_template, request
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load model and scaler
ridge = pickle.load(open('./models/ridge.pkl', 'rb'))
scaler = pickle.load(open('./models/scaler.pkl', 'rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.get('/home')
def home():
    return render_template('home.html')

@app.post('/predict_datapoint')
def predict_datapoint():
    try:
        data = [float(x) for x in request.form.values()]
        final_data = scaler.transform(np.array(data).reshape(1, -1))
        result = ridge.predict(final_data)[0]
        return  render_template("prediction.html", **request.form.to_dict(), result=result)
    except Exception as e:
        return render_template('home.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
