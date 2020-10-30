from task_list.tasks.TaskList import TaskList
from task_list.users.User import User
from task_list.users.Admin import Admin

# instantiate an example task list
tasks = TaskList()
# instantiate an example user
regularUser = User("Regular", "User", 1234)
# instantiate an example admin
adminUser = Admin("Admin", "User", 4246)
