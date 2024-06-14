from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost/scott'
app.config['SECRET_KEY'] = 'my super secret key'
# Initialize datbase
db = SQLAlchemy(app)

# Create a models
class Dept(db.Model):
    DEPTNO = db.Column(db.Integer, primary_key=True)
    DNAME = db.Column(db.String(10), nullable=False)
    LOC = db.Column(db.String(13), nullable=False)

class Emp(db.Model):
    EMPNO = db.Column(db.Integer, primary_key=True)
    ENAME = db.Column(db.String(10), nullable=False)
    JOB = db.Column(db.String(9))
    MGR = db.Column(db.Integer)
    HIREDATE = db.Column(db.DateTime)
    SAL = db.Column(db.Double)
    COMM = db.Column(db.Double)
    DEPTNO = db.Column(db.Integer, db.ForeignKey("DEPT.DEPTNO"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dept')
def view_dept():
    depts = Dept.query.all()
    return render_template('dept.html', depts=depts)

@app.route('/emp')
def view_emp():
    emps = Emp.query.all()
    return render_template('emp.html', emps=emps)

app.run(host='0.0.0.0', port=3000, debug=True)