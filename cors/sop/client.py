from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTTP Request Example</title>
    </head>
    <body>
        <h1>Flask with JavaScript</h1>
        <label for="urlInput">Enter the URL:</label>
        <input type="text" id="urlInput" placeholder="https://example.com/api">
        <button id="requestButton">Send Request</button>
        <p id="responseText"></p>

        <script>
            document.getElementById("requestButton").onclick = function() {
                // Get the URL from the input field
                const url = document.getElementById("urlInput").value;

                if (url) {
                    // Sending a GET request using Fetch API
                    fetch(url)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById("responseText").innerText = JSON.stringify(data);
                        })
                        .catch(error => {
                            document.getElementById("responseText").innerText = 'Error: ' + error;
                        });
                } else {
                    document.getElementById("responseText").innerText = 'Please enter a valid URL.';
                }
            }
        </script>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
