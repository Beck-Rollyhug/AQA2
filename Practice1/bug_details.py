from typing import List
from dataclasses import dataclass

bugType = dict[int, str, int]

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
            ID = 0,
            name = 'Bug',
            status = 0
        )
    ]


    showBugs(bugs)
    action = input('\nshow - show bugs, \nb status s - change status "s" of bug with ID = "b"\ncommand: ')

    match action:
        case 'show':
            showBugs(bugs)
        case command if 'status' in command:
            data = command.split(' ')
            bugID  = int(data[0])
            statusIDx  = int(data[2])
            bugs[bugID].status = statusIDx

            showBugs(bugs)
        case _:
            return
