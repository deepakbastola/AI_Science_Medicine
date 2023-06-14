import base64
import random
from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

coin_states = ["head", "tail"]
current_coin_state = random.choice(coin_states)

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def htmldoc():
    text_below_coin = "Note: Coin flips randomly displaying Head or Tail."
    image_path_head = r"C:\Users\User\Desktop\Microdot\Microdot_modified\coin_head.png"
    image_path_tail = r"C:\Users\User\Desktop\Microdot\Microdot_modified\coin_tail.png"
    encoded_image_head = get_base64_image(image_path_head)
    encoded_image_tail = get_base64_image(image_path_tail)

    return f'''
       <html>
    <head>
        <title>Click the coin to Flip</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
            }}
            .coin {{
                animation: coin-toss 1s ease-in-out;
            }}
            @keyframes coin-toss {{
                0% {{
                    transform: rotateY(0deg);
                }}
                50% {{
                    transform: rotateY(180deg);
                }}
                100% {{
                    transform: rotateY(0deg);
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Click the Coin to Flip</h1>
            <svg width="400" height="400" viewBox="0 0 200 200">
                <a href="/toggle">
                    <image class="coin" xlink:href="data:image/png;base64,{encoded_image_head if current_coin_state == 'head' else encoded_image_tail}" x="5" y="5" width="190" height="190" />
                </a>
            </svg>
            <p>{text_below_coin}</p>  

        </div>
    </body>
</html>
    '''


@app.route('/')
def home(request):
    return htmldoc()


@app.route('/toggle')
def toggle_coin(request):
    global current_coin_state
    current_coin_state = random.choice(coin_states)
    return htmldoc()


app.run(debug=True, port=8008)
