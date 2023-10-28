from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        birth_year = int(request.form['birth_year'])
        birth_month = int(request.form['birth_month'])
        birth_date = int(request.form['birth_date'])

        today = datetime.today()
        birth_datetime = datetime(birth_year, birth_month, birth_date)

        age = today.year - birth_datetime.year - ((today.month, today.day) < (birth_datetime.month, birth_datetime.day))

        return render_template('index.html', age=age)
    return render_template('index.html', age=None)


if __name__ == "__main__":
    app.run(debug=True)
