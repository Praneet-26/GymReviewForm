from crypt import methods
from pyexpat.errors import messages

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        student = request.form['Student']
        gym_location = request.form['gymloc']
        rating = request.form['rating']
        comments = request.form['comments']
        print(student,gym_location,rating,comments)
        if student == '' or gym_location == '':
            return render_template('index.html', message='Please enter required fields')
        return render_template('success.html')

if __name__ == '__main__':
    app.debug = True
    app.run()