from flask import Flask,render_template,request,redirect,session
import os
import mysql.connector


app = Flask(__name__)

app.secret_key=os.urandom(24)

conn = mysql.connector.connect(host="127.0.0.1", user="root", password="",database="edcflask")
cursor = conn.cursor()


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/voltage_divider')
def voltage_divider():
    if 'user_id' in session:
        return render_template('voltage_divider.html')
    else:
        return redirect('/')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    
    if request.method=='POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')
        cursor.execute("""SELECT * FROM `users` where `email` LIKE '{}' AND `password` LIKE '{}' """
                    .format(email,password))
        users = cursor.fetchall()
 
        if len(users)>0:
            session['user_id']=users[0][0]
            return redirect('/home')
        else:
            return redirect('/')



@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES
    (NULL,'{}','{}','{}')""".format(name,email,password))
    conn.commit()
    #Register will also lead to home
    cursor.execute("""SELECT * FROM `users` where `email` LIKE '{}' """ .format(email))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0]
    return redirect('/home')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/calculate_vd', methods=['POST'])
def calculate_vd():
    r1 = int(request.form.get('r1'))
    r2 = int(request.form.get('r2'))
    rc = int(request.form.get('rc'))
    re = int(request.form.get('re'))
    vs = int(request.form.get('vs'))
    beta = int(request.form.get('beta'))


    rth = (r1*r2)/(r1+r2)
    vth = (vs*r2)/(r1+r2)
    ib = (vth-0.7)/(rth + (1+beta)*re)
    ic = beta*ib
    vce = vs-ic*(rc+re)
    

    result = "The current value of Ib is {0}µA , Ic is {1}mA and the voltage at Vce is {2} V".format(ib,ic,vce)

    return render_template("/voltage_divider.html",msg=result)

if __name__=="__main__":
    app.run(debug=True)