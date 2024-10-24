
import webbrowser
from threading import Timer
from flask import Flask

app = Flask(__name__)

# Flask route
@app.route('/')
def index():
    return "Hello, Flask is running!"

# Function to launch browser
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

# Start the Flask server with automatic browser opening
if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run()
