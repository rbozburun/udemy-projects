from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/capture')
def capture_data():
    data = request.get_json()  # Capture the JSON data sent in the request body
    if not data:
        data = {"error": "No data received"}  # Handle cases where no data is sent

    # Log the captured data to the console (optional)
    print(f"Captured Data: {data}")

    # Return a response indicating that the data was captured successfully
    return jsonify({"status": "success", "received_data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
