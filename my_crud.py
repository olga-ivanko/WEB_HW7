from db import session
from models import Group, Student, Professor, Subject, Grade
from sqlalchemy import func
from pprint import pprint
from random import choice, randint
from datetime import datetime


def create(model, name):
    if model == "Group":
        data = Group(group_name=name)

    if model == "Student":
        group_nums = (
            session.query(Group.group_id)
            .select_from(Group)
            .group_by(Group.group_id)
            .all()
        )
        data = Student(student_name=name, group_id=choice(group_nums)[0])

    if model == "Professor":
        data = Professor(professor_name=name)

    if model == "Subject":
        professor_ids = (
            session.query(Professor.professor_id).select_from(Professor).all()
        )
        data = Subject(subject_name=name, professor_id=choice(professor_ids)[0])

    if model == "Grade":
        date_recieved = datetime(
            randint(2022, 2023), randint(1, 12), randint(1, 28)
        ).date()
        subject_ids = session.query(Subject.professor_id).select_from(Subject).all()
        student_ids = session.query(Student.student_id).select_from(Student).all()
        data = Grade(
            grade=int(name),
            student_id=choice(student_ids)[0],
            subject_id=choice(subject_ids)[0],
            date_recieved=date_recieved,
        )

    session.add(data)
    session.commit()
    return f"{model} {name} sucessfuly added"


def read(model):
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Professor":
        data = Professor
    if model == "Subject":
        data = Subject
    if model == "Grade":
        data = Grade

    result = session.query("*").select_from(data).all()
    return result


def update(model, id, name):
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Professor":
        data = Professor
    if model == "Subject":
        data = Subject
    if model == "Grade":
        data = Grade

    result = session.get(data, int(id))
    if model == "Group":
        result.group_name = name
    if model == "Student":
        result.student_name = name
    if model == "Professor":
        result.professor_name = name
    if model == "Subject":
        result.subject_name = name
    if model == "Grade":
        result.grade = int(name)

    session.add(result)
    session.commit()

    return f"succesfuly updated with name: {name}"


def delete(model, id):
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Professor":
        data = Professor
    if model == "Subject":
        data = Subject
    if model == "Grade":
        data = Grade
    result = session.get(data, int(id))
    session.delete(result)
    session.commit()
    return f"{model} with id:{id} is succesfuly removed"


if __name__ == "__main__":
    # pprint(read("Grade"))
    # pprint(update("Grade", "953", "200500"))
    # pprint(create("Professor", "New Professor"))
    # pprint(delete("Grade", "953"))
    # pprint(read("Grade"))
    # pprint(read("Subject"))
    # pprint(update("Student", "53", "Mykola"))
    # pprint(update("Student", "53", "Mykola"))
    #pprint(delete("Professor", "7"))
    # pprint(delete("Subject", "6"))
    # pprint(read("Subject"))
    pprint(read("Professor"))

    # pprint(read("Group"))