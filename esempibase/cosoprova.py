from math import sqrt 
a = sqrt(9)

print("a è uguale a ",a,4, True)

def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(3))
print(switch(5))

class PythonSwitch:
    def day(self, dayOfWeek):

        default = "Incorrect day"

        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "monday"

 

    def case_2(self):
        return "tuesday"

 

    def case_3(self):
        return "wednesday"

   

    def case_4(self):
       return "thursday"

 

    def case_5(self):
        return "friday"

 

    def case_7(self):
        return "saturday"
    
    def case_6(self):
        return "sunday"

   
my_switch = PythonSwitch()

print (my_switch.day(1))

print (my_switch.day(3))
 