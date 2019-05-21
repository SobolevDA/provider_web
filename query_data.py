import pymysql

connections = pymysql.connect('localhost', 'root', 'qwerty', 'provider')
cursor = connections.cursor()


def date_time(date):
    cursor.execute("select unix_timestamp('{}');".format(date))
    date = cursor.fetchall()
    return date[0][0]


