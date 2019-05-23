import pymysql
import xlwt
from datetime import datetime


wb = xlwt.Workbook()
ws = wb.add_sheet('Должники')


connections = pymysql.connect('localhost', 'root', 'qwerty', 'provider')
cursor = connections.cursor()


def date_time(date):
    cursor.execute("select unix_timestamp('{}');".format(date))
    date = cursor.fetchall()
    return date[0][0]


def promiser_customer(id_street, id_service, limit):
        i = 0

        query_sql = 'select distinct customer.name, customer.id, street.name, address.house, address.appart, service.name, customer.balance ' \
            'from street,service, customer,address,link_customer_service ' \
            'where customer.address_id=address.id and address.street_id={} and street.id={} ' \
            'and link_customer_service.service_id={} and service.id={} ' \
            'and link_customer_service.unlink_time is NULL ' \
            'and customer.id=link_customer_service.customer_id and customer.balance <-{} ' \
            'and customer.is_locked  is NULL and customer.is_deleted is NULL;'.format(id_street, id_street, id_service, id_service, limit)

        cursor.execute(query_sql)
        data = cursor.fetchall()
        sort = sorted(data, key=lambda x: x[3])
        for x in sort:
                ws.write(i, 0, x[0])
                ws.write(i, 1, x[1]+793000)
                ws.write(i, 2, x[2])
                ws.write(i, 3, x[3])
                ws.write(i, 4, x[4])
                ws.write(i, 5, x[5])
                ws.write(i, 6, x[6])
                i += 1
        
        wb.save('sheets/{}.xls'.format(datetime.now))
