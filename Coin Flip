######################################################################
#Coin Flip
######################################################################

from microdot import Microdot, Response
app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc():
    coin_text = "Heads" if coin_state == 0 else "Tails"

    return f'''
        <html>
            <head>
                <title>Click to Flip Coin</title>
            </head>
            <body>
                <div>
                    <h1>Click the Coin to Flip</h1>
                    <svg width="200" height="200" viewBox="0 0 200 200">
                        <a href="/toggle">
                            <circle style="fill:#F0E68C" cx="100" cy="100" r="90"/>
                            <text x="50%" y="50%" font-size="24" text-anchor="middle" dy=".3em">{coin_text}</text>
                        </a>
                    </svg>
                </div>
            </body>
        </html>
        '''

coin_state = 0

@app.route('/')
def home(request):
    return htmldoc()

@app.route('/toggle')
def toggle_coin(request):
    global coin_state
    coin_state = 1 - coin_state
    return htmldoc()

app.run(debug=True, port=8008)
