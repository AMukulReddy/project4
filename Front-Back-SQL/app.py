from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('response.html',context='You are in HomePage')



@app.route('/user',methods=['GET'])
def user():
    return render_template('form.html',path='/user-data',form_name='Registration Form')

import pymysql as sql
my_connection = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'project'
)

@app.route('/user-data',methods=['POST'])
def user_data():
    u_id=request.form['u_id']
    u_name=request.form['u_name']
    u_age=request.form['u_age']
    u_salary=request.form['u_salary']

    my_cursor=my_connection.cursor()
    query = ''' 
        insert into user_data(u_id,u_name,u_age,u_salary)
        values(%s,%s,%s,%s);
    '''

    values = (u_id,u_name,u_age,u_salary)
    my_cursor.execute(query,values)
    my_connection.commit()
    return render_template('response.html',context='DATA INSERTED, CHECK IN MYSQL')


@app.route('/view',methods=['GET'])
def view():
    my_cursor=my_connection.cursor()
    query = '''
        select * from user_data;
    '''
    my_cursor.execute(query)
    data = my_cursor.fetchall()
    return render_template('response.html',context=data)

@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html',path='/update-form',form_name='Update Form')

@app.route('/update-form',methods=['POST'])
def update_form():
    u_id = request.form['u_id']
    u_age = request.form['u_age']
    


app.run()
