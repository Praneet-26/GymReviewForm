from flask import Flask, render_template, request
from db.utils import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        student = request.form['Student']
        gym_location = request.form['gymloc']
        student_type = request.form['studenttype']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(student,gym_location,rating,comments,student_type)
        if student == '' or gym_location == '' or student_type == '':

            return render_template('index.html', message='Please enter required fields'),404
        try:
            exec_file('sql/createTable.sql')
            query = """
            INSERT INTO reviews (student, student_type, gym_location, rating, comment)
            VALUES (%s, %s, %s, %s, %s)
            """
            commit(query,(student,student_type,gym_location,rating,comments))
            con = connect()
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM reviews;")
            total_reviews = cur.fetchone()[0]
            con.close()
            return render_template('success.html', message="Review Submitted",Total = total_reviews),200
        except Exception as e:
            print(f"Error occured: {e}")
            return render_template('index.html', message=f'{e}'),404



if __name__ == '__main__':
    app.debug = True
    app.run()