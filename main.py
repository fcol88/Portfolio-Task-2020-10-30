from datetime import datetime

# Task List V1.0

# Author::: 
# Matt Graham

# Description:::
# Learning exercise for CETM65

# Usage:::
# Three objects are instantiated at runtime for your convenience: User regularUser, Admin adminUser and TaskList tasks

# Users and Admins have some (very) basic authentication via the pin property. Enter your pin when you're adding an action to "make sure" someone isn't giving you silly tasks to do.

# A User can add Tasks and display information about themselves, like so:
# regularUser.addTask(aTaskListVariable, "A task to be added", "1234")
# regularUser.whoAmI()

# An Admin can perform the same tasks and also clear the list, like so:

# adminUser.clearList(aTaskListVariable, "4246")

# Tasks have an assigned User, description, created date and a status. When a task is moved to completed, it is given a completed date and the status is changed to "Done".

# The TaskList allows you to show active Tasks, all Tasks, or complete a Task (either on your behalf or on the behalf of another User), like so:

# tasks.showTaskList()
# tasks.showFullTaskList()
# tasks.completeTask()

# When completing a task, if there's only one task in the list, this will be completed automatically. Otherwise, you'll be asked to choose the ID of the task.

# You can instantiate other TaskLists, Users and Admins if you need to - this way you can manage multiple task lists/workloads at once.

#define user class
class User:
    #initialise user with provided first name and last name
    def __init__(self, firstName, lastName, pin):
        self.firstName = firstName
        self.lastName = lastName
        self.pin = pin
        #composited class
        self.created = Audit()

    #decoration which flags pin as a property, aka "getter/setter" situation
    @property
    def pin(self):
        return self.__pin

    #property.setter - in this case when setting pin, send it to __pin
    @pin.setter
    def pin(self, pin):
        if type(pin) != int:
            print("Your pin must be a number (without quotes), Let's set it to 0000 for now.")
            pin = 0
        #if pin is less than zero, set it to 0000
        if pin < 0:
            print("Pin set to 0000")
            self.__pin = "0000"
        #if pin is greater than 9999, set it to 9999 and notify the user
        elif pin > 9999:
            print("Pin set to 9999")
            self.__pin = "9999"
        #otherwise, grab the current value and set it to whatever they've entered
        else:
            self.__pin = str(pin).zfill(4)

    #add task method - accepts the TaskList variable as a parameter and the description of the task
    def addTask(self, taskList, description, pin):
        if pin != self.pin:
            print("Incorrect pin!")
            return
        newTask = Task(self, description)
        #calls the addTask function of the taskList object
        taskList.addTask(newTask)

    def whoAmI(self):
        #uses indices of provided parameters to insert variables into string
        print("First Name: {0} || Last Name: {1}".format(self.firstName, self.lastName))

    # returns user as a string
    def __str__(self):
        return "User: {0} {1}".format(self.firstName, self.lastName)

    # returns code used to instantiate object
    def __repr__(self):
        return "User('{0}','{1}',{2})".format(self.firstName,self.lastName,self.pin)

#define Admin class - inherited from User
class Admin(User):

    #additional functionality specific to Admin - can clear list (alternative call from task list)
    def clearList(self, taskList, pin):
        if(pin != self.pin):
            print("Incorrect pin!")
            return
        taskList.clearList(self)

    #str and repr methods inherited from User

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
            print("Whoops! Did you enter a valid task ID?")

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


#simple class at the moment, but could be expanded to include other fields like "user"
class Audit:
    def __init__(self):
        self.timestamp = datetime.now()
    
    def __str__(self):
        return "Timestamp: {0:%d/%m/%y %H:%M}".format(self.timestamp)

    def __repr__(self):
        return "Audit()"

#instantiate an example task list
tasks = TaskList()
#instantiate an example user
regularUser = User("Matt", "Graham", 1234)
#instantiate an example admin
adminUser = Admin("Gav", "McClary", 4246)