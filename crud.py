from db import session
from models import Group, Student, Professor, Subject, Grade
from sqlalchemy import func
from pprint import pprint
from random import choice

MODELS = {}


def create(model, name):
    if model == "Group":
        data = Group(group_name=name)
    if model == "Student":
        group_nums = (
            session.query(func.max(Group.group_id).label("max_group_id"))
            .select_from(Group)
            .group_by(Group.group_id)
            .all()
        )
        data = Student(student_name=name, group_id=choice(group_nums)[0])
    if model == "Professor":
        data = Professor(professor_name=name)
    if model == "Subject":
        data = Subject(subject_name=name)

    session.add(data)
    session.commit()
    return f"sucessfuly added: {data.student_name}"


def read(model):
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Professor":
        data = Professor
    if model == "Subject":
        data = Subject

    result = session.query("*").select_from(data).all()
    session.commit()
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

    result = session.query(data).get(int(id))
    if model == "Group":
        result.group_name = name
    if model == "Student": 
        result.student_name = name
    if model == "Professor":
        result.professor_name = name
    if model == "Subject":
        result.subject_name = name
    
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
    result = session.query(data).get(int(id))
    session.delete(result)
    session.commit()
    return f"{model} {result.student_name} with id:{id} is succesfuly removed"


if __name__ == "__main__":
    # pprint(create("Student", "Olga"))
    # pprint(update("Student", "53", "Mykola"))
    #pprint(read("Student"))
    #pprint(delete("Student", "53"))
    pass
