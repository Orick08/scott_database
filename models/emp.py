from .models import db

class Emp(db.Model):
    EMPNO = db.Column(db.Integer, primary_key=True)
    ENAME = db.Column(db.String(10), nullable=False)
    JOB = db.Column(db.String(9))
    MGR = db.Column(db.Integer)
    HIREDATE = db.Column(db.DateTime)
    SAL = db.Column(db.Double)
    COMM = db.Column(db.Double)
    DEPTNO = db.Column(db.Integer, db.ForeignKey("DEPT.DEPTNO"))