from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load your model and data
data = pd.read_csv('car_data.csv')

X = data.drop(columns=['Purchased'])
y = data['Purchased']

# Encode categorical variables (e.g., 'Gender') using one-hot encoding
encoder = OneHotEncoder(sparse=False, drop='first')
X_encoded = encoder.fit_transform(X[['Gender']])
X = X.drop(columns=['Gender'])
X = pd.concat([X, pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(['Gender']))], axis=1)

# Train your model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = request.form['gender']
        age = int(request.form['age'])
        annualIncome = int(request.form['annualIncome'])

        # Prepare the input data for prediction
        input_data = [[gender, age, annualIncome]]  # Adjust this based on your data features

        # Make predictions
        prediction = model.predict(input_data)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
