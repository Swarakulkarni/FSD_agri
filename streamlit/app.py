import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Load the Gradient Boosting Regressor model and scaler
model = joblib.load('wbb_gb_model.joblib')
scaler = joblib.load('scaler.joblib')

# Define the order of features
feature_cols = ['AverageRainingDays', 'clonesize', 'honeybee', 'osmia', 'bumbles', 'andrena', 'AverageOfUpperTRange', 'AverageOfLowerTRange']

def main():
    st.title("Yield Prediction")

    # Display an image at the top of the app
    st.image('https://img.freepik.com/premium-photo/spring-grain-concept-agriculture-healthy-eating-organic-food-generative-ai_58409-32489.jpg', use_column_width=True)

    # Create input form below the title
    st.header("Input Features")
    user_input = get_user_input()

    # Add a button to trigger the prediction
    if st.button("Predict"):
        # Scale the input features
        scaled_features = scaler.transform([user_input])

        # Make a prediction
        prediction = model.predict(scaled_features)

        # Display prediction
        st.subheader("Prediction")
        st.success(f"Predicted Yield: {prediction[0]:.2f}")

def get_user_input():
    user_input = []
    for col in feature_cols:
        user_input.append(st.number_input(f"Enter {col}", value=0.0, step=0.1))

    return user_input

if __name__ == '__main__':
    main()