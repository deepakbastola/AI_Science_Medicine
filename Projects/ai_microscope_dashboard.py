from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc():
    return '''
        <html>
            <head>
                <title>AI Microscope Dashboard</title>
            </head>
            <body>
                <h1>AI Microscope Dashboard</h1>
                <div>
                    <ul>
                        <li><a href="/help">Help & Guide</a></li>
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
            </body>
        </html>
    '''

@app.route('/')
def home(request):
    return htmldoc()

@app.route('/help')
def help_guide(request):
    return '''
        <html>
            <head>
                <title>Help & Guide</title>
            </head>
            <body>
                <h2>Instructions to the User / Help Features</h2>
                <p>Welcome to the AI Microscope Dashboard! This dashboard provides various features to assist you with your microscope-related tasks.</p>
                <!-- Add more instructions and information here -->
            </body>
        </html>
    '''

@app.route('/microscope-connection')
def microscope_connection(request):
    return '''
        <html>
            <head>
                <title>Microscope Connection</title>
            </head>
            <body>
                <h2>Microscope Connection</h2>
                <!-- Add components for microscope connection here -->
            </body>
        </html>
    '''

# Add routes for other tabs similarly

app.run(debug=True, port=8008)
