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

@app.route('/airTravelData/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Month Form')

@app.route('/airTravelData/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldMonth'), request.form.get('fld1958'),
                 request.form.get('fld1959'), request.form.get('fld1960'))
    sql_insert_query = """INSERT INTO airTravelImport (Month,Column_1958,Column_1959,Column_1960) VALUES (%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/edit/<int:data_id>', methods=['GET'])
def form_edit_get(data_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airTravelImport WHERE id=%s', data_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', data=result[0])


@app.route('/edit/<int:data_id>', methods=['POST'])
def form_update_post(data_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldMonth'), request.form.get('fld1958'), request.form.get('fld1959'),
                 request.form.get('fld1960'), data_id)
    sql_update_query = """UPDATE airTravelImport t SET t.Month = %s, t.Column_1958 = %s, t.Column_1959 = %s, t.Column_1960 = 
    %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
