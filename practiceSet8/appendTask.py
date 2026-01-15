#  Open tasks.txt in append mode and add a new line "Task Completed!" .

with open("task.txt", "a") as f:
    f.write("Task Completed!")