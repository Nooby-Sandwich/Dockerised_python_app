from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    greeting_message = f"Hello, {name}! Welcome to our Flask app."
    return render_template('greet.html', greeting=greeting_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(3000), debug=True)
