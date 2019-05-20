from flask import Flask, render_template, request
from query_select import service_customer

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', service=service_customer)


@app.route('/count/', methods=['POST'])
def count():
    begin_date = request.form.get('begin_date')
    end_date = request.form.get('end_date')
    print(end_date)
    print(begin_date)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)