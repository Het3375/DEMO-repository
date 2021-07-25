class Employ:
    num_of_leaves=9
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salery=asalary
        self.role=arole



    def func1(self):
        return f"name is { self.name }.salery is { self.salery }. role is { self.role }"

    @classmethod
    def func(cls,numleaves):
        cls.num_of_leaves=numleaves

    @staticmethod
    def mystr(hk):
        dk={"book1":"lion dict",
              "book2":"kingkahan",
              "book3":"crime and panishment"}
        if hk=="list of books":
            print(dk)
        else:
            print("error")





class programer(Employ):
    def __init__(self, aname, asalary, arole,aproggramer):
        self.name = aname
        self.salery = asalary
        self.role = arole
        self.programer=aproggramer



    def printprog(self):
        return f"name is {self.name}.salery is {self.salery}. role is {self.role} ,the programer {self.programer}"


#
het=Employ("het",4555,"proggramer")
#
# shubham=programer("shubham",3577,"programer","python")
#
# rohan=programer("rohan",333,"programer","java")
# print(rohan.printprog())------this is a second class programer--------

# print(het.func1())------this is a main class------
#
# Employ.func(23)         ------this is a class method------
# print(Employ.num_of_leaves)
#
# rohan=het.mystr(" boy ")-----this is a static method-------
# print(rohan)
# print( rohan.mystr(input("list of books\n")))
