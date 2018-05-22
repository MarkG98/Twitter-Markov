from flask import Flask, render_template, request
from markov import Markov


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        username = request.form['username']
        Mgen = Markov()
        res, error = Mgen.markov(username)

        return render_template('markovres.html', res=res, author=username, error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
