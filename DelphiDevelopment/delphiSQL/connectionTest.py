import pymysql as mysql
from pymysql import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='SQLPASSWORD')
        if conn.server_status is 0:
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
