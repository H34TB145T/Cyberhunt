from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('example_template.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    print(f"Location data received: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)