from task_list.tasks.Task import Task
from task_list.Audit import Audit
from task_list.users.Admin import Admin

#define task list class
class TaskList:
    
    # define a private taskList that cannot be easily manipulated at command-line level (not truly private)
    def __init__(self):
        self.__taskList = []
        self.created = Audit()

    # add task to task list
    def addTask(self, task):
      # if task is not a Task, advise the user that they're using the method wrong and return early
        if type(task) != Task:
            print("Incorrect usage of add task. Add from a User or Admin!")
            return
        # otherwise, add the task to the list
        self.__taskList.append(task)

    # clear the task list - not really the intended means of calling the method, but can be done this way
    def clearList(self, user, pin):
        # if the user isn't an admin, prevent them from clearing the list
        if type(user) != Admin or user.pin != pin:
            print("You can't clear the list!")
        else:
            #run clear method on taskList
            self.__taskList.clear()

    # delete a specific task from the list - not really the intended means of calling the method,
    # but can be done this way
    def deleteItem(self, user, pin, id):
        # prevent unauthorised users from deleting
        if type(user) != Admin or user.pin != pin:
            print("You can't delete items!")
        else:
            # if the list is empty, notify the user
            if len(self.__taskList) == 0:
                print("No tasks to delete!")
            # otherwise if it's an invalid ID, tell them that too
            elif id < 1 or id > len(self.__taskList):
                print ("Enter a valid task ID")
            # otherwise delete the item they've specified, adjusting for off-by-one
            else:
                del(self.__taskList[id - 1])
                print("Task deleted")

    # show task list - only active tasks
    def showTaskList(self):
        # print a title
        print("Task List:")
        #loop through tasks in task list
        for task in self.__taskList:
            #if the task hasn't been marked as complete
            if task.status != "Done":
                #call the printTask method with its index in the list and the task itself
                self.printTask(self.__taskList.index(task), task)

    # show the full task list - all tasks
    def showFullTaskList(self):
        # print a title
        print("Task List:")
        # loop through tasks in list
        for task in self.__taskList:
            # print all - no condition checks
            self.printTask(self.__taskList.index(task), task)

    # mark task as completed
    def completeTask(self):
        #if the task list is empty, return early as there's nothing to do
        if len(self.__taskList) == 0:
            print("No tasks to complete!")
            return
        #else if the list only has one item, there's no point offering a prompt, so close the task and return early
        elif len(self.__taskList) == 1:
            #that said, only call completeTask if it's not already marked as done
            if self.__taskList[0].status != "Done":            
                self.__taskList[0].completeTask()
                print("Task marked as completed")
            return

        # otherwise if there's a choice to be made, print the current list of active tasks
        self.showTaskList()
        #wrapped in a try/except to make sure that people entering values either outside the list range or values that aren't a number are dealt with instead of crashing the program
        try:
            #grab the id of the task from the console
            taskToComplete = input("Which task do you want to complete? Enter the ID of the task: ")
            #call the completeTask function and then print the returned string (already completed or now marked as complete)
            #subtract 1 from the ID to prevent off-by-one
            print(self.__taskList[int(taskToComplete) - 1].completeTask())
        except:
            print("You must enter a valid task ID")

    #code used in more than one place so extracted into separate function
    def printTask(self, index, task):
        #uses format to substitute values and a final ternary operator to conditionally add on the completed date if it isn't set to None
        print("Task ID: {0} || Assigned User: {1} {2} || Task: {3} || Status: {4} || Created: {5:%d/%m/%y %H:%M}".format(index + 1, task.user.firstName, task.user.lastName, task.description, task.status, task.created.timestamp), "" if task.completed == None else "|| Completed: {0:%d/%m/%y %H:%M}".format(task.completed.timestamp))

    # returns task list as a string
    def __str__(self):
        taskListString="Created: {0:%d/%m/%y %H:%M} Tasks: ".format(self.created.timestamp)
        # if the list is empty, add a string explaining it's empty
        if (len(self.__taskList)) == 0:
            return taskListString + "None"
        # otherwise, loop through and call the __str__ method on the tasks
        for task in self.__taskList:
            taskListString=taskListString+"{"+str(task)+"},"
        return taskListString[:-1]

    # returns code used to instantiate object
    def __repr__(self):
        return "TaskList()"