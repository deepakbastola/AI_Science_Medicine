```markdown
# SVG Dice Roll

This is a simple web application built with Microdot, a minimalistic web framework for Python. The application allows you to roll multiple dice and displays the results using SVG graphics.

## Prerequisites

- Python 3.6 or higher
- Microdot library

## Installation

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```
   pip install microdot
   ```

## Usage

1. Run the SVG Dice Roll application:

   ```
   python dice_roll.py
   ```

2. Access the application in your web browser at `http://localhost:8009`. You will see one dice displayed on the web page.

3. Click the buttons to roll a specific number of dice. Each dice roll will generate random numbers between 1 and 6, and the results will be displayed using SVG graphics.

4. The background color of each dice SVG will be randomly generated for visual variety.

## Configuration

- Customizing Dice Faces: The `dice_faces` dictionary in the `htmldoc` function in the `dice_roll.py` file contains the SVG code for each dice face. You can customize the appearance of each dice face by modifying the SVG code.

## Contributing

If you are interested in contributing to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!
