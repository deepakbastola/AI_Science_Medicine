import cv2
from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc(content):
    return f'''
        <html>
            <head>
                <title>AI Microscope Dashboard</title>
                <style>
                    ul {{
                        list-style-type: none;
                        margin: 0;
                        padding: 0;
                        overflow: hidden;
                        background-color: #f1f1f1;
                    }}

                    li {{
                        float: left;
                    }}

                    li a {{
                        display: block;
                        color: #000;
                        text-align: center;
                        padding: 14px 16px;
                        text-decoration: none;
                    }}

                    li a:hover {{
                        background-color: #ddd;
                    }}

                    .active {{
                        background-color: #4CAF50;
                        color: white;
                    }}
                </style>
            </head>
            <body>
                <h1>AI Microscope Dashboard</h1>
                <div>
                    <ul>
                        <li><a href="/">Help & Guide</a></li>
                        <li><a href="/microscope-connection">Microscope Connection</a></li>
                        <li><a href="/capture-data">Capture Data</a></li>
                        <li><a href="/archive-data">Archive Data</a></li>
                        <li><a href="/load-data">Load Data</a></li>
                        <li><a href="/view-data">View Data</a></li>
                        <li><a href="/label-data">Label Data</a></li>
                        <li><a href="/train-model">Train Model</a></li>
                        <li><a href="/save-model">Save Model</a></li>
                        <li><a href="/load-model">Load Model</a></li>
                        <li><a href="/test-model">Test Model</a></li>
                        <li><a href="/run-model">Run Model</a></li>
                        <li><a href="/visualize">Visualize</a></li>
                    </ul>
                </div>
                <div>
                    {content}
                </div>
            </body>
        </html>
    '''
#======================================================================================================================================
@app.route('/')
def home(request):
    content = '''
        <h2>Instructions to the User / Help Features</h2>
        <p>Welcome to the AI Microscope Dashboard! This dashboard provides various features to assist you with your microscope-related tasks.</p>
        <p>Here are some instructions to help you navigate through the different features:</p>
        <h3>Connect to Real Instrument</h3>
        <p>Use this feature to establish a connection with your real microscope instrument. Make sure the instrument is properly connected to your computer.</p>
        <h3>Capture Data</h3>
        <p>This feature allows you to capture images or videos from your connected microscope. You can adjust settings such as resolution, exposure, or magnification.</p>
        <h3>Archive Data</h3>
        <p>Archive the captured data, such as images or videos, for future reference or analysis. You can organize and manage your data in this section.</p>
        <h3>Load Data</h3>
        <p>Load previously saved data for viewing or further analysis. This feature allows you to load and access archived data.</p>
        <h3>View Data</h3>
        <p>Visualize and explore the loaded data. You can view images, videos, or other recorded information from your microscope.</p>
        <h3>Label Data</h3>
        <p>Assign labels or annotations to the loaded data. This helps in categorizing or marking specific features or regions of interest.</p>
        <h3>Train Model</h3>
        <p>Train a machine learning model using the labeled data. This enables the model to automatically classify or detect certain patterns or structures in the microscope images.</p>
        <h3>Save Model</h3>
        <p>Save the trained model for future use. This allows you to reuse the trained model without repeating the training process.</p>
        <h3>Load Model</h3>
        <p>Load a pre-trained model to perform classification or detection tasks on new microscope images. This feature allows you to utilize existing models.</p>
        <h3>Test Model</h3>
        <p>Evaluate the performance of the loaded or trained model on test data. This helps in assessing the accuracy and reliability of the model.</p>
        <h3>Run Model on New Images</h3>
        <p>Apply the loaded or trained model on new microscope images captured in real-time. This feature provides real-time analysis and predictions.</p>
        <h3>Visualize Model Outputs</h3>
        <p>Visualize the outputs or predictions of the model on the microscope images. This feature allows you to interpret and analyze the results.</p>
    '''
    return htmldoc(content)

#============================================================================================
# Microscope Connection

def capture_image(folder_name):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return '<h2>Failed to open the webcam.</h2>'

    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    # Save the captured frame as an image file
    filename = f'{folder_name}/captured_image.jpg'
    cv2.imwrite(filename, frame)

    return f'<h2>Image captured successfully and saved in folder: {folder_name}</h2>'

@app.route('/')
def home(request):
    content = '''
        <h2>Instructions to the User / Help Features</h2>
        <!-- Add help content here -->
    '''
    return htmldoc(content)

@app.route('/microscope-connection')
def microscope_connection(request):
    content = '''
        <h2>Microscope Connection</h2>
        <p>Click the button below to capture an image from the microscope and save it in a specific folder.</p>
        <form action="/capture-image" method="POST">
            <button type="submit" name="folder" value="Folder 1">Save in Folder 1</button>
            <button type="submit" name="folder" value="Folder 2">Save in Folder 2</button>
        </form>
    '''
    return htmldoc(content)

@app.route('/capture-image', methods=['POST'])
def capture_image_route(request):
    folder_name = request.form['folder']
    return capture_image(folder_name)

#======================================================================================================================================

# Add routes for other tabs similarly

if __name__ == '__main__':
    app.run(debug=True, port=8008)
