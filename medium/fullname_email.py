
#! Fullname and Email

# Create instand attributes fullname and email in the Employee class

# - Form the fullname by joining the first and last name together, separated by a space
# - Form the email by joining the first an last name together with a . in between, and follow it with @company.com at the end
    # Make sure email is in lowercase

class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def email(self):
        return f"{self.firstname}.{self.lastname}@company.com".lower()
    
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname())
print(emp_2.email())

# Actual

class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + ' ' + lastname
        self.email = '{}.{}@company.com'.format(firstname, lastname).lower()