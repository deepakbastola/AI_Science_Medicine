
```markdown
# Image Dashboard

This is a web application built with Microdot that allows you to explore different visual aspects of an image, including grayscale conversion, channel separation, histogram analysis, and edge detection.


## Features

- **Toggle Grayscale**: Clicking the "Toggle Grayscale" button converts the image between its original color version and a grayscale version.
- **Channel Separation**: The application displays the image's red, green, and blue channels separately, allowing you to visualize each channel's contribution to the overall image.
- **Histogram Analysis**: The application generates and displays a histogram of the image's pixel intensities, providing insights into the distribution of colors.
- **Edge Detection**: The application applies the Canny edge detection algorithm to the image, highlighting the edges and contours.

## Prerequisites

- Python 3.6 or higher
- Microdot library
- PIL (Pillow) library
- OpenCV (cv2) library
- NumPy library
- Matplotlib library

## Installation

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```
   pip install microdot pillow opencv-python numpy matplotlib
   ```

## Usage

1. Run the Image Dashboard application:

   ```
   python image_dashboard.py
   ```

2. Access the application in your web browser at `http://localhost:8008`.

3. Explore the different features of the Image Dashboard by interacting with the buttons and images on the web page.

## Configuration

- Image URL: By default, the application uses a sample image URL. You can modify the `url` variable in the code to use your own image URL.

## Contributing

If you are interested in contributing to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!


Note: The screenshot mentioned in the README can be captured from the application and saved as `image_dashboard_screenshot.png`.
