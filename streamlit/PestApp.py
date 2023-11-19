# app.py
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import joblib
from PIL import Image

st.title("Image Pest Classification App")

# Load pre-trained InceptionV3 model
model = load_model("my_model.h5")

# Streamlit UI for uploading an image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Preprocess the image
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)

    print(predictions)

    maxPos = 0
    maxConfidence = 0.0
    classes = ["ants", "bees", "beetle","catterpillar","earthworms","earwig","grasshopper","moth","slug","snail","wasp","weevil"]
    for i in range (0,12):
        if (predictions[0][i]>maxConfidence):
            maxConfidence = predictions[0][i]
            maxPos=i

    s=classes[maxPos]
    st.success('The output is {}'.format(s))

    st.write("Confidences:")
    for i in range(0,12):
        st.write(classes[i], " ----- ",predictions[0][i]*100)

