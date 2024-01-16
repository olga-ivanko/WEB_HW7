from db import session
from sqlalchemy import asc, desc
from sqlalchemy import select, func
from models import Grade, Group, Student, Subject, Professor
from pprint import pprint


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    result = (
        session.query(
            Student.student_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.student_id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


# Знайти студента із найвищим середнім балом з певного предмета
def select_2():
    result = (
        session.query(
            Student.student_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .filter(Subject.subject_name == "Math")
        .join(Student)
        .join(Subject)
        .group_by(Student.student_id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return result


# Знайти середній бал у групах з певного предмета.
def select_3():
    result = (
        session.query(
            Group.group_id,
            Group.group_name,
            Subject.subject_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),)
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(Subject.subject_name == "Math")
        .group_by(Group.group_id)
        .group_by(Subject.subject_name)
        .order_by(asc(Group.group_id))
        .all()
    )
    return result


# Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    result = (session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"),).select_from(Grade).all())
    return result
    


if __name__ == "__main__":
    print(
        "--- QUERY 01 ---\n 5 students with the highest average score in all subjects:"
    )
    pprint(select_1())
    print("--- QUERY 02 ---\n the student with the highest average score in Math:")
    pprint(select_2())
    print("--- QUERY 03 ---\n average score in Math in groups:")
    pprint(select_3())
    print("--- QUERY 04 ---\n average grade:")
    pprint(select_4())
