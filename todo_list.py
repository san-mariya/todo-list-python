tasks = []
def add_task():
    x = input("Enter task:")
    task = {"Title":x,"done":False}
    tasks.append(task)
    print("Added succesfully!")
def view_task():
    if len(tasks) == 0:
            print("No tasks added") 
    else:
        for i, task in enumerate(tasks,1):
            if task["done"] == True:
                status = " - done"  
            else:
                status = "- pending"
            print(f"{i}. {task['Title']} {status}")
def mark_done():
    if len(tasks) == 0:
        print("No tasks")
    else:
        x = int(input("Enter task to mark done:"))
        if x < 1 or x > len(tasks):
            print("Enter valid number")
        else:
            tasks[x-1]["done"] = True
            print("Task marked done succesfully!")
def delete_task():
    if len(tasks) == 0:
        print("No tasks")
    else:
        x = int(input("Enter task to delete:"))
        tasks.pop(x-1)
        print("Succesfully deleted")
def main():
    while True:
        print("1 - add task\n2 - view task\n3 - mark as done\n4 - delete task\n5 -Exit")
        choice = int(input("Enter choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
main()


