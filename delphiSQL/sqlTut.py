import pymysql.cursors

# Connect to the database

connection = pymysql.connect(host='localhost',database='python_mysql',user='root',password='SQLPASSWORD')
# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # name = 'hi there'
        # email = 'hi again'
        # hapass = 'hello for the last time'
        # sql = "INSERT INTO `Companies` (`name`,`email`, `password`) VALUES (%s, %s, %s)"
        # cursor.execute(sql, (name, email, hapass))
        # connection.commit()


        # Create a new record
        email = ("delphivision@gmail.com",)
        # sql = git reset HEAD~
        cursor.execute(sql, email)
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        result = cursor.fetchall()
        print(result)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    connection.close()
