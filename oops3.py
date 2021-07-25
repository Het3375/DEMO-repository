
# ---------------------------------oprator overloading---------------------
class Employ:
    num_of_leaves=8
    def __init__(self,name,salery,role):
        self.aname=name
        self.aslary=salery
        self.arole=role
    def prinditails(self):
       return f"The Name is {self.aname}. Salary is {self.aslary} and role is {self.arole}"

    @classmethod
    def change_leaves(cls,numleaves):
        cls.num_of_leaves=numleaves

    def __add__(self, other):
        return self.aname+other.aname

    # def __truediv__(self, other):
    #     return self.aslary/other.aslary



emp=Employ("het",456,"hacker")
emp1=Employ(input(),567,"hsdgrtyh")
print(emp+emp1)

# ____________________________abastractmethod_______________________________________

"""
from abc import ABC ,abstractmethod

class shape(ABC):
    def printditails(self):
        return 0

class gym(shape):
    dumbles=67
    weight=34

    def __init__(self):
        self.dumble=45
        self.weight=56


    def printditails(self):
       return self.dumble+self.weight

emp=gym()
print(emp.printditails())
"""