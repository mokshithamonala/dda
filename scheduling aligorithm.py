
def task_scheduling(tasks):
    tasks.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(task[1] for task in tasks)

    slots = [None] * max_deadline
    total_profit = 0

    for task in tasks:
        name, deadline, profit = task

        for i in range(deadline - 1, -1, -1):
            if slots[i] is None:
                slots[i] = name
                total_profit += profit
                break

    return slots, total_profit


tasks = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

schedule, profit = task_scheduling(tasks)
 
print("Scheduled Tasks:", schedule)
print("Total Profit:", profit)
