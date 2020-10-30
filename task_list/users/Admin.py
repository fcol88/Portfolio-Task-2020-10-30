from task_list.users.User import User


# define Admin class - inherited from User
class Admin(User):

    # additional functionality specific to Admin
    # can clear list (alternative call from task list)
    def clearList(self, taskList, pin):
        if(pin != self.pin):
            print("Incorrect pin!")
            return
        taskList.clearList(self, pin)

    # additional functionality specific to Admin
    # delete a specific task from the list
    def deleteItem(self, taskList, pin, id):
        if(pin != self.pin):
            print("Incorrect pin!")
            return
        taskList.deleteItem(self, pin, id)

    # str and repr methods inherited from User
