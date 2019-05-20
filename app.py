from flask import Flask, render_template
from query_select import service_customer

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', service=service_customer)


if __name__ == '__main__':
    app.run(debug=True)