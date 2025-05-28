def scheduling(tasks):
    new_task = {'Javascript': 2300}
    tasks.append(new_task)
    for task in tasks:
        print(sorted(tasks, key =lambda task: list(task.values())))
        
tasks = [
    {'cleaning':1400},
    {'taskname':1800},
    {'taskname':1200}
]

