from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'airTravel'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Air Travel Data Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airTravelImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, airTravelData=result)

@app.route('/view/<int:data_id>', methods=['GET'])
def record_view(data_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airTravelImport WHERE id=%s', data_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', data=result[0])

@app.route('/delete/<int:data_id>', methods=['POST'])
def form_delete_post(data_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM airTravelImport WHERE id = %s """
    cursor.execute(sql_delete_query, data_id)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/cities/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New City Form')

@app.route('/cities/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldName'), request.form.get('fldLat'), request.form.get('fldLong'),
                 request.form.get('fldCountry'), request.form.get('fldAbbreviation'),
                 request.form.get('fldCapitalStatus'), request.form.get('fldPopulation'))
    sql_insert_query = """INSERT INTO tblCitiesImport (fldName,fldLat,fldLong,fldCountry,fldAbbreviation,fldCapitalStatus,fldPopulation) VALUES (%s, %s,%s, %s,%s, %s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
