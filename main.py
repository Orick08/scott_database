from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost/scott'
app.config['SECRET_KEY'] = 'my super secret key'
# Initialize datbase
db = SQLAlchemy(app)

# Create a model
class Dept(db.Model):
    DEPTNO = db.Column(db.Integer, primary_key=True)
    DEPTname = db.Column(db.String(10), nullable=False)
    LOC = db.Column(db.String(13), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dept')
def view_dept():
    depts = Dept.query.all()
    return render_template('dept.html', depts=depts)

app.run(host='0.0.0.0', port=3000, debug=True)