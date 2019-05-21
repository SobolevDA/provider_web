from flask import Flask, render_template, request
from query_select import service_customer, count_dis, ktv_service
from query_data import date_time

app = Flask(__name__)

### main rout

@app.route('/')
def hello_web():
    return render_template('base.html')

### slect service ethernet customer

@app.route('/ethernet/')
def ehernet():
    return render_template('ethernet.html', service=service_customer)

### select count discount 

@app.route('/ethernet/customer/', methods=['POST'])
def ethernet_customer():
    begin = request.form.get('begin')
    begin_date = date_time(begin)

    end = request.form.get('end')
    end_date = date_time(end)

    id_service = request.form.get('services')
    
    discount = count_dis(begin_date, end_date, id_service)

    return render_template('inform_ethernet.html', 
                           discount=discount,
                           begin=begin, end=end,
                           service=service_customer)

### select customer ktv

@app.route('/ktv/')
def ktv():
    return render_template('ktv.html', ktv_service=ktv_service)

### select general customer ktv

@app.route('/ktv/general_ktv/')
def general_ktv():
    return render_template('ktv.html')



if __name__ == '__main__':
    app.run(debug=True)
