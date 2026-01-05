# Object: The real life entities simulated in code are known as objects
# Class: A blueprint of an object

class student:               #class making
    subject = "Python"
    college = "ABC"


stu1 = student()             #object making   
print (stu1.college)         #printing specific properties


#Constrctor(__init__ method):-

def __init__(self):
    print("This is the constructor")


#Class using constrcor:-

class cars:
    def __init__(self, name, model):
        self.name = name,
        self.model = model,


car1 = cars("Marti", "800")
print (car1.name)

#complete example:- 

# Defining a class named Laptop
# A class is a blueprint for creating objects
class Laptop:

    # Class variable (shared by all objects of this class)
    # storage_type belongs to the class, not to individual objects
    storage_type = "ssd"

    # Constructor method
    # __init__ is automatically called when an object is created
    # self refers to the current object
    def __init__(self, RAM, storage):

        # Instance variable
        # RAM value is stored separately for each object
        self.RAM = RAM

        # Instance variable
        # storage value is stored separately for each object
        self.storage = storage

    # Class method
    # @classmethod decorator tells Python that this method
    # works with the class, not with object instances
    @classmethod
    def get_storage_type(cls):

        # cls refers to the class Laptop
        # Accessing the class variable storage_type
        print(f"storage type = {cls.storage_type}")

    # Instance method
    # This method works with object-specific data
    def get_info(self):

        # self refers to the current object (l1)
        # self.RAM → instance variable
        # self.storage → instance variable
        # self.storage_type → class variable (accessed via object)
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

# Creating an object of Laptop class
# l1 is an instance (object) of Laptop
# "16gb" is passed to RAM, "512gb" is passed to storage
l1 = Laptop("16gb", "512gb")

# Calling the class method using the class name
# This prints the shared storage type for all laptops
Laptop.get_storage_type()
