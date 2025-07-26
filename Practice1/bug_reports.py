def showBugs(bugs, new = -1):
    priority = ['low', 'medium', 'high']
    for i, bug in enumerate(bugs):
        print(f'Ошибка {i}, - {priority[bug]}{' (new)' if i == new else ''}')

def addBug(priority, bugs):
    bugs.append(priority)
    return bugs

def removeFirstLowBug(bugs):
    bugs.remove(0)
    return bugs

def sortBugs(bugs):
    bugs.sort()
    return bugs

def task4():
    # 0, 1, 2 = "low", "medium", "high"
    bugs = [0, 1, 2, 1, 2, 2]
    showBugs(bugs)
    action = input('\nshow - show bugs, \nadd p - add bug with p priority, \nremove - remove first low-priority bug, \nsort - sort bugs by priority, \nquit - quit console \ncommand: ')

    match action:
        case 'show':
            showBugs(bugs)
        case command if 'add' in command:
            p = int(command.split(' ')[1])
            updatedBugs = addBug(p, bugs)
            showBugs(updatedBugs, len(updatedBugs) - 1)
        case 'remove':
            updatedBugs = removeFirstLowBug(bugs)
            showBugs(updatedBugs)
        case 'sort':
            updatedBugs = sortBugs(bugs)
            showBugs(updatedBugs)
        case _:
            return
