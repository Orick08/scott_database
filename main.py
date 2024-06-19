from flask import Flask, render_template

from models.models import db

from routes.dept import dept_bp, new_dept_bp, edit_dept_bp
from routes.emp import emp_bp, new_emp_bp, edit_emp_bp

app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost/scott'
app.config['SECRET_KEY'] = 'my super secret key'
# Initialize datbase
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(dept_bp)
app.register_blueprint(new_dept_bp)
app.register_blueprint(edit_dept_bp)

app.register_blueprint(emp_bp)
app.register_blueprint(new_emp_bp)
app.register_blueprint(edit_emp_bp)


app.run(host='0.0.0.0', port=3000, debug=True)