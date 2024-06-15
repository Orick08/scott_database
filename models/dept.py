from .models import db

class Dept(db.Model):
    DEPTNO = db.Column(db.Integer, primary_key=True)
    DNAME = db.Column(db.String(10), nullable=False)
    LOC = db.Column(db.String(13), nullable=False)