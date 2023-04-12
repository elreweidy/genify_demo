from flask import Flask, request, jsonify
import pickle
import xgboost as xgb
import pandas as pd

# initializing the flask app
app = Flask(__name__)

# loading the model
with open('xgp_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data
    data = request.get_json(force=True)
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_dict(data)
    
    # One-hot-encode the categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        df = pd.concat([df, pd.get_dummies(df[col], prefix=col)], axis=1)
        df.drop(col, axis=1, inplace=True)
    
    # Make predictions
    dmatrix = xgb.DMatrix(df)
    predictions = model.predict(dmatrix)
    
    # Return the predictions
    return jsonify(predictions.tolist())


if __name__ == '__main__':
    app.run(debug=True)
