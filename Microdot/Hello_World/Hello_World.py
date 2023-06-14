from microdot import Microdot, Response
app = Microdot()

@app.route('/')
def hello(request):
    return Response('Hello, World!')

app.run(port=8008)
