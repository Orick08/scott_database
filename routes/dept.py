from flask import Blueprint, render_template
from models.dept import Dept

dept_bp = Blueprint('dept', __name__)
new_dept_bp = Blueprint('new_dept', __name__)

@dept_bp.route('/dept')
def view_dept():
    depts = Dept.query.all()
    return render_template('dept.html', depts=depts)

@new_dept_bp.route('/dept/new')
def new_dept():
    pass

