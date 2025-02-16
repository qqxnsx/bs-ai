import numpy as np
import cv2
import tensorflow as tf
import os

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Configuration parameters
IMG_HEIGHT = 224
IMG_WIDTH = 224
NUM_CLASSES = 4
MODEL_PATH = "brain_tumor_model.h5"

# Define class labels
tumor_classes = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# Function to preprocess an image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Load trained model
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
else:
    print("Error: Model file not found.")

# Function to predict tumor type
def predict_tumor(image_path):
    if not os.path.exists(image_path):
        print("Error: Image file not found.")
        return
    
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    print(f"Predicted Tumor Type: {tumor_classes[predicted_class]} ({confidence * 100:.2f}% confidence)")

# Example usage
image_path = "sample_brain_scan.jpg"  # Replace with an actual image path
predict_t
