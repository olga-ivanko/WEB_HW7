import argparse
from my_crud import create, read, update, delete

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action")
parser.add_argument("-m", "--model")
parser.add_argument("-n", "--name")
parser.add_argument("-id", "--id")

args = parser.parse_args()

action = args.action
model = args.model
name = args.name
id = args.id


def action_func():
    if action == "create":
        return create(model, name)
    elif action == "list":
        return read(model)
    elif action == "update":
        return update(model, id, name)
    elif action == "remove":
        return delete(model, id)
    else:
        return "try again"


if __name__ == "__main__":
    # print(sys.path)
    print(action_func())
# py my_script.py --action create -m Professor --name 'Boris Jonson' створення вчителя
# py my_script.py --action list -m Professor показати всіх вчителів
# py my_script.py --action list --model Professor показати всіх вчителів
# py my_script.py --action update -m Professor --id 8 --name 'Andry Bezos' оновити дані вчителя з id=3
# py my_script.py --action remove -m Professor --id 8 видалити вчителя з id=3
