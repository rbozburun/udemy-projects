from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <html>
        <head>
            <title>Target App</title>
        </head>
        <body>
            <h1>Welcome to the Target App</h1>
            <button onclick="alert('Button clicked!')" style="width:100px; height:30px">Click Me</button>
        </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, port=5000)