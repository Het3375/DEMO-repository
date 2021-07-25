# >>>>>>>>>maps,reduse,filters in python<<<<<<<<<



# items=[1,2,343,5,67,8]
#
# def func(a):
#     return a*a
#
# square=list(map(func,items))
# print(square)


# map,filter syntax: (function,iterable)
#
#
# fk=[1,2,3,4,5,6,7,8,9,10]
# def is_greater5_num(num):
#     return num>5
#
#
# gr_than_5=list(filter(is_greater5_num,fk))
# print(gr_than_5)
#
#
#
# from functools import reduce
#
# list1=[1,23,3,4,5]
# num=reduce(lambda x,y:x+y,list1)
#
# print(num)
#




# >>>>>>> decorators in python<<<<<<<<<<<
"""
def func1():
    print("subscribe now")
func2=func1
del func1
func2()

def func(num):
    if num==1:
        return print
    if num==0:
        return int

a=func(0)
print(a)

def func(num):
     num("this")

func(print)


def dec1(func1):
    def nowexc():
        print("exuting now")
        func1()
        print("executed")
    return nowexc
@dec1
def who_is_het():
    print("het is a good boy")

who_is_het()

"""

# >>>>>>classes<<<<<<
"""
class student:
    pass

harry=student()
larry=student()


harry.std=12
harry.section=2
harry.name="harry"
larry.name="larry"
print(harry.section,larry)

"""


# >>>>>>>>>>share class and objects attributes>>>>>>>
""""
class Employ:
    number_of_units=8
    pass

harry=Employ()
larry=Employ()

harry.name="harry"
harry.salery=8900
harry.section=5

larry.name="larry"
larry.salery=5778
larry.section=56

print(Employ.number_of_units)
print(Employ.__dict__)
Employ.number_of_units=9
print(Employ.__dict__)
print(Employ.number_of_units)
"""



#
# class Employ:
#     num_of_lives=8
#
#
#     def __init__(self,aname,aclass,amarks):
#         self.name=aname
#         self.dclass=aclass
#         self.marks=amarks
#
#     def students(self):
#      return f"student name is { self.name } ,student class is { self.dclass },student marks is { self.marks }"
#
#
#
#
#
#
# harry =Employ("het", 12, 33.33)
#
#
# print(harry.students())
#
# a=4
# b=5
#
# (a,b)=(b,a)
#
# print(b)
#
#
#
#
#
#

