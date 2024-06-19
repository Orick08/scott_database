from flask import Blueprint, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from models.models import db
from models.dept import Dept
from models.emp import Emp

emp_bp = Blueprint('emp', __name__)
new_emp_bp = Blueprint('new_emp', __name__)

@emp_bp.route('/emp')
def view_emp():
    emps = Emp.query.all()
    return render_template('emp.html', emps=emps)

class NewEmpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 10)])
    job = StringField('Job', validators=[DataRequired(), Length(1,8)])
    mng = IntegerField('MNG')
    hiredate = DateField('Hire Date', validators=[DataRequired()])
    sal = FloatField('Salary', validators=[DataRequired()])
    comm = FloatField('COMM')
    dept = SelectField('Department', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Submit')

@new_emp_bp.route('/emp/new', methods=['GET', 'POST'])
def new_emp():
    # Create a new emp
    form = NewEmpForm()
    depts = Dept.query.all()
    form.dept.choices = [(dept.DEPTNO, f"{dept.DNAME} | {dept.LOC}") for dept in depts]
    if form.validate_on_submit():
        emp = Emp(ENAME=form.name.data,JOB=form.job.data
                  ,MGR=form.mng.data,HIREDATE=form.hiredate.data,
                  SAL=form.sal.data,COMM=form.comm.data,DEPTNO=form.dept.data)
        db.session.add(emp)
        db.session.commit()
        return redirect('/emp')
    
    # Render new emp form
    return render_template('new_emp.html', form=form)
