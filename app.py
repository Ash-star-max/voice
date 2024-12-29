from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Here you can add database storage logic
    print("Received form data:", data)
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)