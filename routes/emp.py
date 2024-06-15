from flask import Blueprint, render_template
from models.emp import Emp

emp_bp = Blueprint('emp', __name__)
new_emp_bp = Blueprint('new_emp', __name__)

@emp_bp.route('/emp')
def view_emp():
    emps = Emp.query.all()
    return render_template('emp.html', emps=emps)

@new_emp_bp.route('/emp/new')
def new_emp():
    pass
