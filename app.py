import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("cat_dog_cnn.keras")

st.title("🐱🐶 Cat vs Dog Classifier")
st.write("Upload an image and let the CNN predict whether it is a cat or dog.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image")

    # Preprocessing
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Prediction
    prediction = model.predict(image)[0][0]

    if prediction > 0.5:
        st.success(f"🐶 Dog — Confidence: {prediction * 100:.2f}%")
    else:
        st.success(f"🐱 Cat — Confidence: {(1 - prediction) * 100:.2f}%")