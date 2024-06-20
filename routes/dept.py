from flask import Blueprint, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length
from models.models import db
from models.dept import Dept

dept_bp = Blueprint('dept', __name__)
new_dept_bp = Blueprint('new_dept', __name__)
edit_dept_bp = Blueprint('edit_dept', __name__)
delete_dept_bp = Blueprint('delete_dept', __name__)

class DeleteDeptForm(FlaskForm):
    id = HiddenField('DEPTNO', validators=[DataRequired()])
    submit = SubmitField('Eliminar')

@dept_bp.route('/dept')
def view_dept():
    form = DeleteDeptForm()
    depts = Dept.query.all()
    return render_template('dept.html', depts=depts, delete_form=form)


class NewDeptForm(FlaskForm):
    name = StringField("DEPT Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired(), Length(1, 13)])
    submit = SubmitField("Submit")

@new_dept_bp.route('/dept/new', methods=['GET', 'POST'])
def new_dept():
    # Create a new dept
    form = NewDeptForm()
    if form.validate_on_submit():
        dept = Dept(DNAME=form.name.data,LOC=form.location.data)
        db.session.add(dept)
        db.session.commit()
        return redirect('/dept')
    
    # Render new dept form
    return render_template('new_dept.html', form=form)

# Edit dept
class EditDeptForm(FlaskForm):
    id = HiddenField("DEPTNO", validators=[DataRequired()])
    name = StringField("DEPT Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired(), Length(1, 13)])
    submit = SubmitField("Submit")

@edit_dept_bp.route('/dept/edit/<id>', methods=['GET', 'POST'])
def edit_dept(id):
    # Edit dept
    form = EditDeptForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('Im going to redirect')
        edit_dept = Dept.query.get(form.id.data)
        edit_dept.DEPTNO = form.id.data
        edit_dept.DNAME = form.name.data
        edit_dept.LOC = form.location.data
        db.session.commit()
        return redirect('/dept')
    
    # Render edit dept form
    dept = Dept.query.get(id)
    if dept is None:
        return redirect('/dept')
    form.id.data = dept.DEPTNO
    form.name.data = dept.DNAME
    form.location.data = dept.LOC
    return render_template('edit_dept.html', form=form)

# Delete dept
@delete_dept_bp.route('/dept/delete', methods=['POST'])
def delete_dept():
    form = DeleteDeptForm()
    if form.validate_on_submit():
        dept = Dept.query.get(form.id.data)
        if dept is None:
            return redirect('/dept')
        db.session.delete(dept)
        db.session.commit()
    return redirect('/dept')
