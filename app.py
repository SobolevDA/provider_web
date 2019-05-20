from flask import Flask, render_template, request
from query_select import service_customer, count
from query_date import date_time

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', service=service_customer)


@app.route('/count/', methods=['POST'])
def count():
    begin_date = request.form.get('begin_date')
    begin_date = date_time(begin_date)

    end_date = request.form.get('end_date')
    end_date = date_time(end_date)

    service_id = request.form.get('id_name.id')
    print(service_id)

    print(end_date)
    print(begin_date)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)