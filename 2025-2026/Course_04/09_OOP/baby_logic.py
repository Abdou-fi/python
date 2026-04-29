# BABY LOGIC
class Baby:                     # we define a class called Baby, which will represent a baby and its behaviors
    
    """A class representing a baby"""
    # class variables
    still_a_baby = True             # we set the still_a_baby class variable to True, indicating that the baby is still a baby
    hungry = True                   # we set the hungry class variable to True, indicating that the baby is hungry
    diaper_needs_changing = True    # we set the diaper_needs_changing class variable to True, indicating that the baby's diaper needs changing

    def __init__(self, name, age=1):    # constructor method, called when we create a new Baby object, self is a reference to the object being created, 
                                        # name is a parameter that we pass in when creating the baby
        self.name = name                # we set the name attribute of the baby to the value of the name parameter
        self.age = age                  # we set the age attribute of the baby to the value of the age parameter
      
    def start_cry(self):            # we define a method called start_cry, which will be called when the baby starts crying
        print(f"{self.name} says: WAAAAAAAHHHH")

    def end_cry(self):                                      # we define a method called end_cry, which will be called when the baby stops crying
        print(f"{self.name} says: Hmmm... I'm feeling better now.")     

    def start_sleep(self):                                  # we define a method called start_sleep, which will be called when the baby starts sleeping
        print(f"{self.name} says: Zzzzzzz...")

    def end_sleep(self):                                    # we define a method called end_sleep, which will be called when the baby wakes up from sleep
        print(f"{self.name} says: Good Morning!")         
    
    def state(self):                                        # we define a method called state, which will print the current state of the baby based on its attributes
        if (self.still_a_baby):        # we use a while loop to continuously check the baby's state, and a with statement to manage the baby's behavior based on its state
            if (self.hungry or self.diaper_needs_changing):
                self.end_sleep()
                self.start_cry()
            else:
                self.end_cry()
                self.start_sleep()      


Jameel = Baby("Jameel")               # we create a new Baby object named Jameel and assign it to the variable new_baby
Jameel.hungry = False                      # we set the hungry attribute of the new_baby object to False, indicating that Jameel is no longer hungry
Jameel.diaper_needs_changing = False       # we set the diaper_needs_changing attribute of the new_baby object to False, indicating that Jameel's diaper no longer needs changing   

# while (Jameel.still_a_baby):        # we use a while loop to continuously check the baby's state, and a with statement to manage the baby's behavior based on its state
#     if (Jameel.hungry or Jameel.diaper_needs_changing):
#         Jameel.end_sleep()
#         Jameel.start_cry()
#     else:
#         Jameel.end_cry()
#         Jameel.start_sleep()

Child2 = Baby("Child2", age=2)    # we create another Baby object named Child2 with an age of 2 and assign it to the variable Child2
Child2.still_a_baby = False       # we set the still_a_baby attribute of the Child2 object to False, indicating that Child2 is no longer a baby 

if (Child2.still_a_baby):        # we use a while loop to continuously check the baby's state, and a with statement to manage the baby's behavior based on its state
    if (Child2.hungry or Child2.diaper_needs_changing):
        Child2.end_sleep()
        Child2.start_cry()
    else:
        Child2.end_cry()
        Child2.start_sleep()

Child3 = Baby("Aymen")                  # we create a new Baby object named Aymen and assign it to the variable new_baby
Child3.hungry = True                    # we set the hungry attribute of the new_baby object to True, indicating that Aymen is hungry
Child3.diaper_needs_changing = True     # we set the diaper_needs_changing attribute of the new_baby object to True, indicating that Aymen's diaper needs changing

Child3.state()