🐱🐶 Cat vs Dog Image Classification using CNN

A Deep Learning project that uses a Convolutional Neural Network (CNN) to classify images as either Cat or Dog. The trained model is integrated with a Streamlit web application, allowing users to upload an image and receive a real-time prediction.

🚀 Project Overview

This project demonstrates an end-to-end Deep Learning workflow:

Image Dataset → Preprocessing → CNN Model → Model Training → Validation → Prediction → Streamlit Deployment

The model learns visual features such as shapes, edges, textures, and patterns from cat and dog images and uses these features to classify new images.

🎯 Objective

The main objective is to build an image classification system that can:

- Identify whether an uploaded image is a Cat 🐱 or Dog 🐶
- Process and normalize input images
- Train a CNN using TensorFlow/Keras
- Evaluate model performance using validation data
- Make predictions on completely new images
- Provide an interactive web interface using Streamlit

🧠 Model Architecture

The CNN consists of:

- Convolutional layers for extracting image features
- MaxPooling layers for reducing spatial dimensions
- Global Average Pooling for reducing parameters
- Dense layer for learning higher-level features
- Dropout for reducing overfitting
- Sigmoid output layer for binary classification

Architecture

Input Image (256 × 256 × 3)
          ↓
Conv2D (32 filters)
          ↓
MaxPooling2D
          ↓
Conv2D (64 filters)
          ↓
MaxPooling2D
          ↓
Conv2D (128 filters)
          ↓
MaxPooling2D
          ↓
GlobalAveragePooling2D
          ↓
Dense (128)
          ↓
Dropout (0.5)
          ↓
Dense (1, Sigmoid)
          ↓
Cat / Dog

🔄 Data Preprocessing

Before feeding images into the CNN:

1. Images are resized to 256 × 256 pixels
2. Pixel values are normalized from 0–255 to 0–1
3. A batch dimension is added before prediction

Normalization helps the neural network train more effectively.

⚙️ Training

The model was compiled using:

- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Evaluation Metric: Accuracy
- Epochs: 15

During training, the model achieved approximately 82% validation accuracy at its best point.

The training results also showed signs of overfitting at later epochs, which is an important part of the model evaluation process.

📊 Model Performance

The model initially performed close to random guessing (~50% accuracy). After improving the CNN architecture, it successfully learned meaningful visual patterns.

The best validation accuracy reached approximately:

~82%

Further improvements could be achieved using:

- Data augmentation
- Early stopping
- Learning-rate tuning
- Transfer learning with pretrained models such as MobileNetV2 or EfficientNet

🌐 Streamlit Application

The trained CNN is integrated into a Streamlit application.

Users can:

1. Upload a ".jpg", ".jpeg", or ".png" image
2. View the uploaded image
3. Preprocess the image automatically
4. Get a Cat/Dog prediction
5. View the prediction confidence

🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- OpenCV
- Pillow
- Matplotlib
- Streamlit
- Google Colab
- Git & GitHub

📁 Project Structure

cat-dog-classifier/
│
├── app.py
├── cat_dog_cnn.keras
├── requirements.txt
├── README.md
└── screenshots/
    └── streamlit_app.png

▶️ Run the Project Locally

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>

2. Navigate to the project directory

cd cat-dog-classifier

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

📸 Application Preview

Add a screenshot of your Streamlit application here:

![Streamlit App](screenshots/streamlit_app.png)

🔮 Future Improvements

- Add data augmentation
- Improve validation accuracy
- Use transfer learning
- Add prediction confidence visualization
- Support more animal classes
- Deploy the application publicly

👨‍💻 Author

Dipayan Hazra

This project was developed as part of my journey in Deep Learning and Artificial Intelligence.

⭐ If you found this project useful

Feel free to ⭐ star the repository and explore the project.