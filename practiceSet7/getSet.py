# Create a class Employee with a private attribute _salary .
# Use @property to define a getter for salary .
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries


class Employee:
    def __init__(self, salary):
        self._salary = salary


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, val):
        if (val < 0):
            print("enter valid salary")
        else:
            self._salary = val


e = Employee(7)
print(e.salary)
e.salary = 9
print(e.salary)