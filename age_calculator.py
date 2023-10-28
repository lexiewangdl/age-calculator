from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        birth_year = int(request.form['birth_year'])
        birth_month = int(request.form['birth_month'])
        birth_date = int(request.form['birth_date'])
        age = calculate_age(birth_year, birth_month, birth_date)
        return render_template('index.html', age=age)
    return render_template('index.html', age=None)


def calculate_age(year, month, day):
    today = datetime.today()
    birthdate = datetime(year, month, day)

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    return f"{years} years, {months} months, {days} days"


if __name__ == '__main__':
    app.run(debug=True)
