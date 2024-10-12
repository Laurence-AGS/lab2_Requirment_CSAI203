from flask import Flask, render_template,request,session,redirect,url_for
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'Super_Secret_Key'

def days_until_birthday(birthdate_str, date_format = '%Y-%m-%d'):
    birthdate = datetime.strptime(birthdate_str, date_format)
    today = datetime.now()
    current_year_birthday = birthdate.replace(year = today.year)
    if current_year_birthday < today:
        next_birthday = current_year_birthday.replace(year = today.year + 1)
    else:
        next_birthday = current_year_birthday
    days_left = (next_birthday - today).days
    return days_left

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == "POST":
        name = request.form.get("student's name")
        B_date = request.form.get("birth date")
        session['name'] = name
        session['B_date'] = B_date
        return redirect(url_for('results'))
    return render_template('index.html')


@app.route('/results', methods = ['GET'])
def results():
    if 'name' in session and 'B_date' in session:
        days_result = days_until_birthday(session['B_date'])
        name = session['name']
        session.clear()
        return render_template('results.html', name = name, days = days_result)
    else:
        return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True)