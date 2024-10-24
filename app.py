
import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='client/build')

# Serve React app
@app.route('/')
def serve_react_app():
    return send_from_directory(app.static_folder, 'index.html')

# Example API route
@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data to be used by React
    return jsonify({"message": "Hello from Flask API!"})

# Fallback for all other routes to serve React app
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

# Start the Flask server
if __name__ == "__main__":
    app.run()
