import pymysql as mysql
from pymysql import Error
from python_mysql_dbconfig import read_db_config


def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        MySQLConnection = mysql.connect
        conn = MySQLConnection(**db_config)

        # if conn.Error is None:
        #     print('connection established.')
        # else:
        #     print('connection failed.')
        print(conn.server_status)

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')


if __name__ == '__main__':
    connect()
