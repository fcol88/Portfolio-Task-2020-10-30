from task_list.Audit import Audit
from task_list.tasks.Task import Task


# define user class
class User:
    # initialise user with provided first name and last name
    def __init__(self, firstName, lastName, pin):
        self.firstName = firstName
        self.lastName = lastName
        self.pin = pin
        # composited class
        self.created = Audit()

    # decoration which flags pin as a property, aka "getter/setter" situation
    @property
    def pin(self):
        return self.__pin

    # property.setter - in this case when setting pin, send it to __pin
    @pin.setter
    def pin(self, pin):
        if type(pin) != int:
            print("Your pin must be a number " +
                  "(without quotes), Let's set it to " +
                  "0000 for now.")
            pin = 0
        # if pin is less than zero, set it to 0000
        if pin < 0:
            self.__pin = "0000"
            print("Pin set to 0000")
        # if pin is greater than 9999, set it to 9999 and notify the user
        elif pin > 9999:
            self.__pin = "9999"
            print("Pin set to 9999")
        # otherwise, grab the current value
        # and set it to whatever they've entered
        else:
            zeroPaddedPin = str(pin).zfill(4)
            self.__pin = zeroPaddedPin
            print("Pin set to " + zeroPaddedPin)

    # add task method - accepts the TaskList variable
    # as a parameter and the description of the task
    def addTask(self, taskList, description, pin):
        if pin != self.pin:
            print("Incorrect pin!")
            return
        newTask = Task(self, description)
        # calls the addTask function of the taskList object
        taskList.addTask(newTask)

    def whoAmI(self):
        # uses indices of provided parameters to insert variables into string
        print("First Name: {0} || Last Name: {1}"
              .format(self.firstName, self.lastName))

    # returns user as a string
    def __str__(self):
        return "User: {0} {1}".format(self.firstName, self.lastName)

    # returns code used to instantiate object
    def __repr__(self):
        return "User('{0}','{1}',{2})".format(self.firstName, self.lastName,
                                              self.pin)
