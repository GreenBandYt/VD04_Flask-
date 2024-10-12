from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/page2/')
def Page2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


