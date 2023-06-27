# Microscope Image Classification Project

This is a Python Flask application for classifying microscope images. The application includes functionalities to visualize and label images, train a convolutional neural network (CNN) model, and predict the class of new images.

## Libraries Used
* Flask
* NumPy
* Pandas
* Matplotlib
* cv2 (OpenCV)
* scikit-learn
* Keras/TensorFlow

## Project Structure

This Flask web application has several endpoints:

* `/`: Home page where users can upload images for classification.
* `/view-data`: This endpoint is used to visualize the uploaded data.
* `/label-data`: This endpoint allows users to manually label the data.
* `/train-model`: This endpoint trains a CNN model using the labeled data.
* `/save-model`: This endpoint saves the trained model to disk.
* `/load-model`: This endpoint loads a saved model from disk.
* `/test-model`: This endpoint evaluates the model's performance on a test set.
* `/run-model`: This endpoint classifies a new image using the trained model.

## How to Use

1. Start the Flask server: `python main.py`.
2. Visit `http://localhost:8008/` in your browser to use the web application.

## Future Enhancements

* Improve the image visualization and labeling process.
* Improve the CNN model and train it on a larger dataset.
* Create an endpoint to handle batch prediction.
* Deploy the application to a production environment.

Please feel free to contribute to this project and enhance its features.
 Project completed by myself and [Francis Boateng](https://github.com/fBoatengs/AI_in_SCience_and_Medicine)
