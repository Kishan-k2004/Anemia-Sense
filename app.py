import pickle
import numpy as np
from flask import Flask, request, render_template

# Load the saved model
model = pickle.load(open("model.pkl", "rb"))

# Create Flask app
app = Flask(__name__)

# Route for home page
@app.route("/")
def index():
    return render_template("index.html")

# Route for prediction
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Retrieve values from form
        features = [float(request.form['feature1']),
                    float(request.form['feature2']),
                    float(request.form['feature3']),
                    float(request.form['feature4']),
                    float(request.form['feature5'])]
        
        # Convert to numpy array and reshape
        input_data = np.array([features])
        
        # Get prediction from model
        prediction = model.predict(input_data)
        
        return render_template("predict.html", prediction_text=f"Predicted Value: {prediction[0]}")
    
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
