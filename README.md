# 🥔 Potato Disease Classification

Detect **Late Blight** and **Early Blight** in potato plants using deep learning and computer vision.

## 🌱 Overview

This project provides an excellent solution for farmers and agriculturists to identify common potato diseases from leaf images. By leveraging deep learning and image processing techniques, the application classifies potato leaf images as **Healthy**, **Late Blight**, or **Early Blight**—helping users take rapid action to protect their crops.

## 🚀 Features

- **Image Upload**: Easily upload potato leaf images for instant diagnosis.
- **Accurate Classification**: Utilizes advanced deep learning models for high accuracy.
- **User-Friendly Interface**: Simple and intuitive web-based user experience.
- **Real-Time Feedback**: Get disease predictions in seconds.

## 🛠️ Technology Stack

| Layer             | Technology                       | Purpose                                   |
|-------------------|----------------------------------|-------------------------------------------|
| Backend           | **Python**, **TensorFlow**, **Keras** | Model training and inference              |
| Image Processing  | **OpenCV**                       | Preprocessing and feature extraction      |
| Frontend          | **JavaScript**, **HTML**, **CSS**| Interactive web application               |
| API/Server        | **Node.js**                      | REST API and backend integration          |

## 📸 How It Works

1. **Collect Data**: Gather potato leaf images (healthy and diseased).
2. **Train Model**: Use deep learning (TensorFlow & Keras) to train a classifier.
3. **Process Image**: Preprocess input images using OpenCV for better results.
4. **Predict**: Upload an image via the web app—model predicts the disease type instantly.

## ✨ Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/mr360cool/Potato-DiseasE-Classification.git
   
2. **Install dependencies**
  - *Refer to the respective requirements.txt or package.json files for python and Node.js*
    ```bash
    # For Python dependencies
    pip install -r requirements.txt
    # For Node.js dependencies
    npm install
    
3. **Run the application**
    ```bash
    # Start the backend server(Replace 'main.py' with the correct file for your backend)
    python main.py
    # Launch the frontend for user interaction
    npm start
