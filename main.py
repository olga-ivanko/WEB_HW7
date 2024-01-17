import argparse
from crud import create, read, update, delete
import pprint

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


def main():
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
    pprint(main())
# poetry run python main.py --action create -m Professor --name 'Boris Jonson' створення вчителя
# poetry run python main.py --action list -m Professor показати всіх вчителів
# py main.py --action list -m Professor показати всіх вчителів
# py main.py --action update -m Professor --id 3 --name 'Andry Bezos' оновити дані вчителя з id=3
# py main.py --action remove -m Professor --id 3 видалити вчителя з id=3
