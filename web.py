from flask import Flask

app = Flask(__name__)

@app.route('/') # << Python decorators
def hello():
    return 'Hello everyone in this class'

if __name__ == "__main__":
    app.run()

# For external use, do port forwarding and use external IP address with
# forwarded port
