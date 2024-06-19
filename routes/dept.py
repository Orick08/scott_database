from flask import Blueprint, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from models.models import db
from models.dept import Dept

dept_bp = Blueprint('dept', __name__)
new_dept_bp = Blueprint('new_dept', __name__)

@dept_bp.route('/dept')
def view_dept():
    depts = Dept.query.all()
    return render_template('dept.html', depts=depts)


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

