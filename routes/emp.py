from flask import Blueprint, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, FloatField, SelectField, HiddenField, BooleanField ,SubmitField
from wtforms.validators import DataRequired, Length
from models.models import db
from models.dept import Dept
from models.emp import Emp

emp_bp = Blueprint('emp', __name__)
new_emp_bp = Blueprint('new_emp', __name__)
edit_emp_bp = Blueprint('edit_emp', __name__)
delete_emp_bp = Blueprint('delete_emp',__name__)

class DeleteEmpForm(FlaskForm):
    id = HiddenField('EMPNO', validators=[DataRequired()])
    submit = SubmitField('Eliminar')

@emp_bp.route('/emp')
def view_emp():
    form = DeleteEmpForm()
    emps = Emp.query.all()
    return render_template('emp.html', emps=emps, delete_form=form)

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
        flash("Empleado agregado con éxito.")
        return redirect('/emp')
    
    # Render new emp form
    depts = Dept.query.all()
    form.dept.choices = [(dept.DEPTNO, f"{dept.DNAME} | {dept.LOC}") for dept in depts]
    return render_template('new_emp.html', form=form)

#Edit emp
class EditEmpForm(FlaskForm):
    id = HiddenField("EMPNO", validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(1, 10)])
    job = StringField('Job', validators=[DataRequired(), Length(1,8)])
    mng = IntegerField('MNG')
    hiredate = DateField('Hire Date', validators=[DataRequired()])
    sal = FloatField('Salary', validators=[DataRequired()])
    comm = FloatField('COMM')
    dept = SelectField('Department', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Submit')

@edit_emp_bp.route('/emp/edit/<id>', methods=['GET', 'POST'])
def edit_emp(id):
    form = EditEmpForm()
    depts = Dept.query.all()
    form.dept.choices = [(dept.DEPTNO, f"{dept.DNAME} | {dept.LOC}") for dept in depts]
    # Edit emp on database
    if form.validate_on_submit():
        print('Im going to redirect')
        edit_emp = Emp.query.get(form.id.data)
        edit_emp.ENAME = form.name.data
        edit_emp.JOB = form.job.data
        edit_emp.MGR = form.mng.data
        edit_emp.HIREDATE = form.hiredate.data
        edit_emp.SAL = form.sal.data
        edit_emp.COMM = form.comm.data
        edit_emp.DEPTNO = form.dept.data
        db.session.commit()
        flash("Empleado editado con éxito.")
        return redirect('/emp')
    
    print('No redirect')
    # Render edit emp form
    emp = Emp.query.get(id)
    if emp is None:
        flash("No se ha encontrado el empleado.")
        return redirect('/emp')
    
    form.id.data = emp.EMPNO
    form.name.data = emp.ENAME
    form.job.data = emp.JOB
    form.mng.data = emp.MGR
    form.hiredate.data = emp.HIREDATE
    form.sal.data = emp.SAL
    form.comm.data = emp.COMM
    form.dept.data = emp.DEPTNO
    return render_template('edit_emp.html', form=form)

# Delete EMP
@delete_emp_bp.route('/emp/delete', methods=['POST'])
def delete_emp():
    form = DeleteEmpForm()
    if form.validate_on_submit():
        emp = Emp.query.get(form.id.data)
        if emp is None:
            return redirect('/emp')
        db.session.delete(emp)
        db.session.commit()
    flash("Empleado eliminado con éxito.")
    return redirect('/emp')
