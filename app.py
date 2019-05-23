from flask import Flask, render_template, request
from query_select import service_customer, count_dis
from query_select import ktv_service, ktv_customer, id_city, id_street
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
    return render_template('ktv.html',
                           ktv_service=ktv_service,
                           id_city=id_city, 
                           id_street=id_street)

### select general customer ktv


@app.route('/ktv/general_ktv/', methods=['POST'])
def general_ktv():
    service_id = request.form.get('sevice_id')
    count_customer_ktv = ktv_customer(service_id)
    return render_template('ktv_general_inform.html', 
                           count_customer_ktv=count_customer_ktv, 
                           ktv_service=ktv_service)


#@app.route('/ktv/promiser_ktv/', methods=['POST'])
#def promiser_ktv():


if __name__ == '__main__':
    app.run(debug=True)
