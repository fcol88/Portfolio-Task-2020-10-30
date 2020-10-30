from task_list.Audit import Audit


# define Task class
class Task:
    # initialise Task - uses datetime imported library
    def __init__(self, user, description):
        self.status = "To Do"
        self.created = Audit()
        self.completed = None

        self.user = user
        self.description = description

    # complete task - usually called from TaskList
    def completeTask(self):
        # if the task hasn't already been marked as completed...
        if self.status != "Done":
            # ...mark it as completed...
            self.status = "Done"
            # ...and set the completed time to now...
            self.completed = Audit()
            # ...then return a string to be printed
            return "Task marked as completed"
        # if the task has been completed, return a string to be printed
        return "Task already completed!"

    # code used in more than one place so extracted into separate function
    # code moved to Task to conform with SRP
    def printTask(self, index):
        # uses format to substitute values and a final ternary
        # operator to conditionally add on the completed date
        # if it isn't set to None
        taskId = "Task ID: {0}".format(index + 1)
        user = " || Assigned User: {0} {1}".format(self.user.firstName,
                                                   self.user.lastName)
        task = " || Task: {0}".format(self.description)
        status = " || Status: {0}".format(self.status)
        created = " || Created: {0:%d/%m/%y %H:%M}"\
            .format(self.created.timestamp)
        completed = ""

        if self.completed is not None:
            completed = " || Completed: {0:%d/%m/%y %H:%M}"\
                .format(self.completed.timestamp)

        print(taskId + user + task + status + created + completed)

    # returns task as a string
    def __str__(self):

        description = "Task: Description={0}".format(self.description)
        status = ", Status={0}".format(self.status)
        user = ", User={0} {1}".format(self.user.firstName, self.user.lastName)
        created = ", Created={0:%d/%m/%y %H:%M}".format(self.created.timestamp)
        completed = ""
        if self.completed is not None:
            completed = ", Completed: {0:%d/%m/%y %H:%M}".format(
                self.completed.timestamp)

        return description + status + user + created + completed

    # returns code used to instantiate object
    def __repr__(self):
        return "Task(user,'{0}')".format(self.description)
