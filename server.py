from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<int:num>')
@app.route('/<int:num>/<color>')
def index(num = 3, color = 'blue'):
    return render_template('index.html', num = num, color = color)


if __name__=="__main__": 
    app.run(debug=True)