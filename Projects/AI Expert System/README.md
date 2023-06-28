# Medical Image Analysis with Chest X-rays

This project aims to perform medical image analysis using chest X-ray images to detect and classify pneumonia. It includes various functionalities such as dataset loading, data visualization, neural network training, model evaluation, and a question-and-answer (Q&A) system.

## Dataset

The dataset used in this project is the PneumoniaMNIST dataset, which consists of chest X-ray images classified into two categories: normal and pneumonia. The dataset is preprocessed and stored as numpy arrays for easy access and manipulation. The dataset is split into training, validation, and test sets.

To load the dataset, click on the "Load Dataset" button, which will display a sample image and a montage of images from the dataset.

## Data Visualization

Data visualization is an essential step in understanding the dataset. This project provides functionality to generate a histogram of the label distribution in the dataset. Click on the "Generate Histogram" button to visualize the frequency of normal and pneumonia labels.

Additionally, you can explore the RGB channels of a randomly selected image from the dataset. Click on the "View RGB Channels" button to visualize the original image and its separate RGB channels.

## Neural Network Training

The project utilizes a pre-trained ResNet-50 model for pneumonia classification. The model's final fully connected layer is modified to match the number of classes in the dataset. To train the neural network, click on the "Train Neural Network" button.

The training process involves loading the dataset, splitting it into train, validation, and test sets, creating data loaders, freezing the pre-trained layers, modifying the fully connected layer, defining the loss function and optimizer, and training the model for a specified number of epochs.

## Model Saving and Loading

Once the neural network is trained, you can save the model for future use. Click on the "Save Model" button to save the trained model to a file named "model.pt". The model's state dictionary is saved, allowing you to load the model later using the "Load Model" button.

## Model Evaluation

To evaluate the performance of the trained model, click on the "Test Accuracy" button. This will load the test dataset and calculate the accuracy of the model on the test images. The accuracy is displayed as a percentage.

## Q&A System

The project includes a question-and-answer (Q&A) system that provides answers to specific questions. To ask a question, enter it in the provided text input box and click the "Q&A" button. The system currently supports questions about the capital of France, the painter of the Mona Lisa, the square root of 64, the symptoms of pneumonia, and how pneumonia is diagnosed. The system will display the corresponding answer based on the question asked.

## Requirements

To run this project, you need the following dependencies:

- medmnist
- torch
- torchvision
- pandas
- numpy
- scikit-learn
- matplotlib
- scikit-image
- ipywidgets

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
```

2. Change into the project directory:

```
cd your-repo
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the Jupyter Notebook or Python script to interact with the functionalities provided by the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The PneumoniaMNIST dataset used in

 this project is provided by [MedMNIST](https://github.com/MedMNIST/MedMNIST) project.
- The pre-trained ResNet-50 model is part of the torchvision package.
- This project is for educational purposes only and should not be used for clinical decision-making.

Feel free to explore the project, experiment with different functionalities, and contribute to its development by submitting pull requests.

If you encounter any issues or have suggestions for improvement, please open an issue in the repository.

Thank you for your interest in this project!
