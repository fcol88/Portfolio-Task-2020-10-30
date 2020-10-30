# Portfolio Task 2020-10-30 (Week 4)

Learning exercise for CETM65

## Task List V1.2

### Description

Learning exercise for CETM65

### Usage

If you're running in an IDE where the interpreter hangs around after running main.py, happy days.

If you're running from command line, you might want to try:

` python -i main.py `

or 

` python3 -i main.py `

depending on your version.

Three objects are instantiated at runtime for your convenience: User regularUser, Admin adminUser and TaskList tasks

Users and Admins have some (very) basic authentication via the pin property. Enter your pin when you're adding an action to "make sure" someone isn't giving you silly tasks to do.

A User can add Tasks and display information about themselves, like so:

```
regularUser.addTask(aTaskListVariable, "A task to be added", "1234")
regularUser.whoAmI()
```

An Admin can perform the same tasks, as well as also clearing the list and deleting an individual item by ID (if there are items to delete) like so:

```
adminUser.clearList(aTaskListVariable, "4246")
adminUser.deleteItem(aTaskListVariable, "4246", 1)
```

Tasks have an assigned User, description, created date and a status. When a task is moved to completed, it is given a completed date and the status is changed to "Done".

The TaskList allows you to show active Tasks, all Tasks, or complete a Task (either on your behalf or on the behalf of another User), like so:

```
tasks.showTaskList()
tasks.showFullTaskList()
tasks.completeTask()
```

When completing a task, if there's only one task in the list, this will be completed automatically. Otherwise, you'll be asked to choose the ID of the task.

You can instantiate other TaskLists, Users and Admins if you need to - this way you can manage multiple task lists/workloads at once.
