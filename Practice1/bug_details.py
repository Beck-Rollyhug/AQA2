from typing import List
from dataclasses import dataclass


@dataclass
class Bug:
    ID: int
    name: str
    status: int


def showBugs(bugs):
    status = ['backlog', 'in work', 'test', 'solved']
    for bug in bugs:
        print(f'{bug.name} {bug.ID} - {status[bug.status]}\n')


def task5():

    bugs: List[Bug] = [
        Bug(
            ID=0,
            name='Bug',
            status=0
        )
    ]

    showBugs(bugs)
    action = input(
        '\n"show" \t\t - Show bugs \n"b status s" \t - Change status "s" of bug with ID = "b" \n\n Status:\n 0 \t - backlog \n 1 \t - in work \n 2 \t - test \n 3 \t - solved \ncommand: ')

    match action:
        case 'show':
            showBugs(bugs)
        case command if 'status' in command:
            data = command.split(' ')
            bugID = int(data[0])
            statusIDx = int(data[2])
            bugs[bugID].status = statusIDx

            showBugs(bugs)
        case _:
            return
