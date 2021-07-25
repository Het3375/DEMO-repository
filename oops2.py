"""
this is a multiple inheritance
"""

"""
class Employ:

    def __init__(self,aname,asalery,arole):
        self.name=aname
        self.salery=asalery
        self.role=arole
    def myprog(self):
        return f"your name is{self.name}.your salery is{self.salery}.your role is{self.role}"





class Cool:
    def __init__(self, aname,acool):
        self.name = aname
        self.cool=acool

    def mystr(self):
        return f"your name is{self.name}. this man is so {self.cool}"



class Progrramer(Employ,Cool):
    languaje="python"

    def prit(self):
     print(self.languaje)

karan=Progrramer("karan",3556,"proggramer")
karan=Cool("KARAN","COOL")
print(karan.mystr())
"""


# ------------mulitiline inheritance-------------------------

"""
class dad:
    dance=1
    volleyball=1
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class son(dad):
    dance=2
    volleyball=5
    def isvooly(self):
        return f"yes i dance osammm...{self.dance} no of times"

class Grandson(son):
    dance=7
    volleyball = 8
    guitar=3

    def isking(self):
        return f"yes i dance kingly.....{self.dance} no of times"


harry=dad()
het=son()
larry=Grandson()


"""

# -----------------------------this is a protect and private __________________________________
"""

class Employ:
    var=8
    _pi=45
    __king=4567

    def __init__(self,name,role):
        self.aname=name
        self.arole=role
    def prit(self):
        return f"name is{self.aname}.role is{self.arole}"


emp=Employ("het","proggramer")
print(emp._Employ__king)
"""

# __________________________________________-super constructor____________________________________
""""
class A:
    classvar1="i am in class A"

    def __init__(self):
        self.var1="i am a insider classA"
        self.classvar1="instract var in A"
        self.special="this is a special"

class B(A):
   classvar1= "I am in class B"

   def __init__(self):

       self.var1 = "I am inside class B's constructor"
       self.classvar1 = "Instance var in class B"
       super().__init__()
       print(super().classvar1)

a=A()
b=B()
print(b.special,b.var1,b.classvar1)
"""


