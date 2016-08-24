from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import flask
import sys, os, subprocess
from tempfile import TemporaryFile
import pickle
import json
import requests
# import search *IMPORTANT
import pymysql.cursors
from passlib.hash import sha256_crypt
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    resp = flask.Response(json_data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    # return search.delphiSearch('iptest.xml') *IMPORTANT
    # subprocess.call(['python', 'search.py', 'iptest.xml'])
    # outfile.seek(0)

@app.route("/yo")
def helloworld():
    return "YO"

@app.route("/mediaWikiRevisions", methods=['GET'])
def getRevision():

    baseOne = "https://www.mediawiki.org/w/api.php?action=query&titles="
    basetwo = "&prop=revisions&format=json&rvlimit=max&rvprop=timestamp|content|comment"
    title = request.args.get("title")
    requestUrl = baseOne + title + basetwo
    revJson = requests.get(requestUrl).json()
    pageID = list(revJson['query']['pages'])
    revisionArray = revJson['query']['pages'][pageID[0]]
    return flask.jsonify(revisionArray)
@app.route("/createCompany", methods=['GET','POST'])
def createCompany():
    # TODO Make method SQL INJECTION SAFE
    error = None
    if request.method == 'POST':
        try:
            name = str(request.form['name'])
            # email = str(request.form['email'])
            hapass = sha256_crypt.encrypt(request.form['password'])
            connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
            emailalreadyexists = False
            try:
                with connection.cursor() as cursor:
                    email = str(request.form['email'])
                    desired = (email,)
                    checkst = "SELECT * FROM Companies WHERE email= %s"
                    cursor.execute(checkst, desired)
                    reut = cursor.fetchone()
                    if not reut:
                        sql = "INSERT INTO `Companies` (`name`,`email`, `password`) VALUES (%s, %s, %s)"
                        cursor.execute(sql, (name, email, hapass))
                        connection.commit()
                    else:
                        emailalreadyexists = True
                    cursor.close()

            finally:
                if emailalreadyexists:
                    return "Email Account already exists"
                with connection.cursor() as cursor:
                    sql = "Select * from Companies"
                    cursor.execute(sql)
                    rv = tuple(cursor.fetchall())
                    connection.close()
                    if not rv:
                        return "UNSUCCESSFUL"
                    else:
                        return rv[len(rv) - 1][1]
        except KeyError:
            return "Cannot find Form Keys"
    else:
        error = 'Make a Post Request'
    return error

@app.route("/authenticateCompany", methods=['GET','POST'])
def authComp():
    if request.method == 'POST':
        authenticated = False
        try:
            email = str(request.form['email'])
            connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
            try:
                with connection.cursor() as cursor:
                    input = (email,)
                    checkst = "SELECT * FROM Companies WHERE email= %s"
                    cursor.execute(checkst, email)
                    tupleCompany = cursor.fetchone()
                    authenticated = sha256_crypt.verify(request.form['password'],tupleCompany[3])
            finally:
                connection.close()
        except KeyError:
            return "Make sure to enter email and password"
        finally:
            # TODO Make the Return Value a Dictionary
            return str(authenticated)





    # parameters:
    #     name
    #     email
    #     password
    #     cmail
@app.route("/createEmployee", methods=['POST'])
def createEmp():
    try:
        email = str(request.form['email'])
        name = str(request.form['name'])
        cmail = str(request.form['cmail'])
        hapass = sha256_crypt.encrypt(request.form['password'])
        connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
        emailalreadyexists = False
        with connection.cursor() as cursor:
            desired = (email,)
            checkst = "SELECT * FROM Employees WHERE email= %s"
            cursor.execute(checkst, desired)
            reut = cursor.fetchone()
            if not reut:
                sql = "INSERT INTO `Employees` (`company_email`,`name`,`email`, `password`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (cmail, name, email, hapass))
                connection.commit()
            else:
                emailalreadyexists = True
            cursor.close()

    except KeyError:
        return "Make sure to Pass in All Paramters name, email, password and cmail"
    finally:
        if emailalreadyexists:
            return "Email Account already exists"
        with connection.cursor() as cursor:
            desired = (email,)
            checkst = "SELECT * FROM Employees WHERE email= %s"
            cursor.execute(checkst, desired)
            rv = tuple(cursor.fetchone())
            connection.close()
            if not rv:
                return "UNSUCCESSFUL"
            else:
                return rv[2]


@app.route("/authenticateEmployee", methods=['GET','POST'])
def authEmp():
    if request.method == 'POST':
        authenticated = False
        try:
            email = str(request.form['email'])
            connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
            try:
                with connection.cursor() as cursor:
                    input = (email,)
                    checkst = "SELECT * FROM Employees WHERE email= %s"
                    cursor.execute(checkst, input)
                    tupleCompany = cursor.fetchone()
                    authenticated = sha256_crypt.verify(request.form['password'],tupleCompany[4])
            finally:
                connection.close()
        except KeyError:
            return "Make sure to enter email and password"
        finally:
            # TODO Make the Return Value a Dictionary
            return str(authenticated)
@app.route("/changeEmployeePassword", methods=['GET', 'POST'])
def changePass():
    if request.method == 'POST':
        try:
            email = request.form['email']
            newpass = request.form['newpass']
            query = "UPDATE Employees SET password=%s WHERE email=%s;"
            desired = (sha256_crypt.encrypt(newpass), email,)
            connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query, desired)
                    connection.commit()
            finally:
                connection.close()
        except KeyError:
            return "Make sure to enter email and password"
        return str(True)

@app.route("/createProject", methods=['POST'])
def createProj():
    try:
        name = str(request.form['name'])
        companyID = request.form['company_id']
        connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Projects` (`name`,`company_id`) VALUES (%s, %s)"
            cursor.execute(sql, (name, companyID))
            connection.commit()
            cursor.close()
    except KeyError:
        return "Make sure to Pass in All Paramters name, company id, patent writer id"
    finally:
        with connection.cursor() as cursor:
            desired = (name,)
            checkst = "SELECT * FROM Projects WHERE name= %s"
            cursor.execute(checkst, desired)
            rv = tuple(cursor.fetchone())
            connection.close()
            if not rv:
                return "UNSUCCESSFUL"
            else:
                return rv[1]
@app.route("/addPatentWritertoProject", methods=['POST'])
def addPtoProj():
    try:
        p_id = request.form['pa_id']
        pr_id = request.form['pr_id']
        connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
        writernonexistent = False
        with connection.cursor() as cursor:
            desired = (p_id,)
            checkst = "SELECT * FROM Patent_Writers WHERE patent_writer_id= %s"
            cursor.execute(checkst, desired)
            reut = cursor.fetchone()
            if reut:
                query = "UPDATE Projects SET patent_writer_id=%s WHERE proj_id=%s;"
                cursor.execute(query, (pr_id, p_id))
                connection.commit()
                query = "UPDATE Patent_Writers SET project_id=%s WHERE patent_writer_id=%s"
                cursor.execute(query, (pr_id, p_id))
            else:
                writernonexistent = True
            cursor.close()

    except KeyError:
        return "Make sure to Pass in All Paramters project id, patent writer id"
    finally:
        if writernonexistent:
            return "Patent Writer Does Not Exist. Please Create one"
        else:
            return "Writer Added to Project"

@app.route("/createPatentWriter", methods=['POST'])
def createPW():
    try:
        email = str(request.form['email'])
        name = str(request.form['name'])
        hapass = sha256_crypt.encrypt(request.form['password'])
        connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
        emailalreadyexists = False
        with connection.cursor() as cursor:
            desired = (email,)
            checkst = "SELECT * FROM Patent_Writers WHERE email= %s"
            cursor.execute(checkst, desired)
            reut = cursor.fetchone()
            if not reut:
                sql = "INSERT INTO `Patent_Writers` (`name`,`email`,`password`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, hapass))
                connection.commit()
            else:
                emailalreadyexists = True
            cursor.close()

    except KeyError:
        return "Make sure to Pass in All Paramters name, email, password and cmail"
    finally:
        if emailalreadyexists:
            return "Email Account already exists"
        else:
            return "Patent Writer Created"

@app.route("/addProjectURL", methods=['POST'])
def addProjURL():
    try:
        url = str(request.form['proj_url'])
        proj_id = request.form['proj_id']
        query = "UPDATE Projects SET proj_url=%s WHERE proj_id=%s;"
        desired = (url, proj_id,)
        connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, desired)
                connection.commit()
        finally:
            connection.close()
    except KeyError:
        return "Make sure to enter project id and project url"
    return str(True)


# `project_id`
# `date`
# `sig_ord`
# `text`
# `key_alterations`

@app.route("/createMajorIteration", methods=['POST'])
def createMajorIter():
    try:
        pr_id = request.form['pr_id']
        date = request.form['date']
        sig_ord = request.form['sig_ord']
        text = str(request.form['text'])
        key_alterations = str(request.form['key_alterations'])

        connection = pymysql.connect(host='localhost', database='python_mysql', user='root', password='SQLPASSWORD')
        with connection.cursor() as cursor:
            # Get Last Iteration Number
            checkst = "SELECT iteration_number FROM M_Iterations WHERE project_id= %s ORDER BY iteration_number"
            cursor.execute(checkst, pr_id)
            last_iter = cursor.fetchone()
            sql = "INSERT INTO `M_Iterations` (`pr_id`,`iteration_number`, 'date', 'sig_ord', 'text', 'key_alterations') VALUES (%s, %s, %s, %s,%s,%s,)"
            cursor.execute(sql, (pr_id, last_iter, date, sig_ord, text, key_alterations))
            connection.commit()
            cursor.close()
    except KeyError:
        return "Make sure to Pass in All Paramters project id, date, sig_ord, text, key_alterations"
    finally:
        return "Successfully added Iteration"
if __name__ == "__main__":
    app.run()
