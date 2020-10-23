from task_list.Audit import Audit

#define Task class
class Task:
    #initialise Task - uses datetime imported library
    def __init__(self, user, description):
        self.status = "To Do"
        self.created = Audit()
        self.completed = None
        
        self.user = user
        self.description = description

    #complete task - usually called from TaskList
    def completeTask(self):
        #if the task hasn't already been marked as completed...
        if self.status != "Done":
            # ...mark it as completed...
            self.status = "Done"
            # ...and set the completed time to now...
            self.completed = Audit()
            # ...then return a string to be printed
            return "Task marked as completed"
        #if the task has been completed, return a string to be printed
        return "Task already completed!"

    # returns task as a string
    def __str__(self):
        return "Task: Description={0}, Status={1}, User={2} {3} Created={4:%d/%m/%y %H:%M}".format(self.description, self.status, self.user.firstName, self.user.lastName, self.created.timestamp) + ("" if self.completed == None else " || Completed: {0:%d/%m/%y %H:%M}".format(self.completed.timestamp))

    # returns code used to instantiate object
    def __repr__(self):
        return "Task(user,'{0}')".format(self.description)