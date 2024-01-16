from db import session
from sqlalchemy import asc, desc
from sqlalchemy import select, func
from models import Grade, Group, Student, Subject, Professor
from pprint import pprint

def select_1():
   result = session.query(Student.student_name, func.round(func.avg(Grade.grade), 2).label('avg_grade') ).select_from(Grade).join(Student).group_by(Student.student_id).order_by(desc('avg_grade')) .limit(5).all()
   return result


if __name__ == "__main__":
    pprint(select_1())
