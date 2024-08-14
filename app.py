from flask import Flask, render_template, redirect, url_for, request, session, flash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key'  # Make sure to set a secret key

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == app.config['TEACHER_USERNAME'] and password == app.config['TEACHER_PASSWORD']:
            session['user'] = 'teacher'
            return redirect(url_for('teacher'))

        elif username == app.config['STUDENT_USERNAME'] and password == app.config['STUDENT_PASSWORD']:
            session['user'] = 'student'
            return redirect(url_for('student'))

        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

@app.route('/teacher')
def teacher():
    if session.get('user') == 'teacher':
        return render_template('teacher.html')
    return redirect(url_for('login'))

@app.route('/student')
def student():
    if session.get('user') == 'student':
        return render_template('student.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
