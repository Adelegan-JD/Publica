class Student:      # This creates a class calleed Student
    def __init__(self, name, course, level):        # This initializes the class, and creates the referencing
        print("Creating a new student...")
        self.name = name  # This assigns name to the object
        self.course = course        # This assigns course to the object
        self.level = level      # This assigns level to the object
        print(f'Student {name} has been created!')

kemi = Student("Kemi Adebayo", "Computer Science", 300)


class NigerianStudent:
    def __init__(self, name, state, course, level):
        print(f"Step 1: Creating student object")
        self.name = name  # This assigns name to the object
        self.state_of_origin = state        # # This assigns state to the object
        self.course = course   # This assigns course to the object
        self.level = level      #This assigns level to the object
        self.student_id = self.generate_id()      #This generates a unique id for the object
        print(f'Step 6: {self.name} from {self.state_of_origin} is ready! Your matric number is {self.student_id}')

    def generate_id(self):
        import random
        return f'UNIOGUN{random.randint(10000, 99999)}'

# When an object is created, this happens
ayo = NigerianStudent('Ayo Daniel', 'Ogun', 'Machine Learning', 400)

# To print each attribute, call the function name
print(ayo.name)

# Another Example
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f'{self.name} joined {self.network} network')


    def buy_airtime(self, amount):
        self.airtime += amount  # self ensures it gets the RIGHT person
        return f"{self.name} now has NGN{self.airtime} airtime"


# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")

# Each person's actions affect only affect their own account
print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(500))

print(abeeb.airtime)
print(onisemo.airtime)

# Defining the attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

# Creating a studentt object
Fathia = Student("Fathia Abdul", "Biochemistry", 400, "Ogun State")

# Accessing Attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.level)
print(Fathia.state_of_origin)









































