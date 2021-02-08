class Employee:

   total_Employee=0
   raise_amount=1.03

   # init method take self Argument as default
   # No need to specifically declare self

   def __init__(self,first,last,pay):   
      # Four variables will be initialised
      self.first=first
      self.last=last
      self.pay=pay
      self.email=first + "." + last +"@company.com"
      Employee.total_Employee+=1
      super().__init__()
   
   # Method FullName returns the fullName of the employee
   # Regular Method--
   def fullName(self):
      return self.first+' '+self.last
   
   # Class MEthod
   @classmethod # <-- This is called as Decorator
   def apply_raise(cls,amount):
      cls.raise_amount=amount

# Instance Variables
emp1=Employee('Omkar','Khilari',50000)
emp2=Employee('Corey','Schafer',60000)

print(emp1.first,emp1.pay)

# Both ways below are correct
print(emp1.fullName())
print(Employee.fullName(emp2)) #Here we will need to specify self

print(Employee.total_Employee)

