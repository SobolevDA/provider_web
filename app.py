from flask import Flask, render_template, request
from query_select import service_customer, count_dis
from query_date import date_time

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', service=service_customer)


@app.route('/ethernet/', methods=['POST'])
def count():
    begin = request.form.get('begin')
    begin_date = date_time(begin)
    print(begin_date)

    end = request.form.get('end')
    end_date = date_time(end)
    print(end_date)

    id_service = request.form.get('services')
    print(id_service)
    
    discount = count_dis(begin_date, end_date, id_service)
    print(discount)

    return render_template('inform.html', 
                           discount=discount,
                           begin=begin, end=end,
                           service=service_customer)


if __name__ == '__main__':
    app.run(debug=True)