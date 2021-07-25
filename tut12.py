#lemda function or annonymous function
"""
lamda syntax
var name=lamda probability:condition
"""
"""""
def func1(a,b):
  return a+b


minus=lambda a,b:a+b

print(minus(4,5))

def minus(a,b):
    return a+b

print(minus(4,5))

def myfunc(n):
    return lambda a:a*n

myvar=myfunc(4)
def myfunc(m):
    return lambda a:a*m

myvar=myfunc(5)
print(myvar(10))
container=myfunc(7)
print(container(2))
print(myvar(6))
"""

#what is a fstring in python

# name="het"
# love="python"
# hobby="codding"
#
# print(f'my name is {name} \n my love is{love}\n my hooby is{hobby}')

import time

# k=0
# while(k<1000):
#     print("het is a good boy")
#     k+=1
# print("loop is",time.time(),"secound")




# x=-1
#
# if x<0:
#     raise Exception("sorry somthing got error")
#


# x="hello"
#
# if not type(x) is int:
#     raise  TypeError("only integers are allowed")
#
#
# f=open()
#
# print(f.tell())
# print(f.readline())


# def myfunc(n):
#     return lambda a:a+n
#
# het=myfunc(3)
# print(het(13))


# args and kwargs
# def myfunc(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# myfunc("harry","het","rohan","ravi","kadu")


def myfunc(normal,*argsname,**kwargskiller):
    print(normal)
    for item in argsname:
        print(item)

    print("\nthese are a killers")
    for key,value in kwargskiller.items():
        print(key,value)



# het=myfunc("het","rohan","ravi","kadu","jay")
# print(*het)
#
normal="i am a pythoner"
har=["het","rohan","ravi","kadu","jay"]
kw={"het":"is a good boy","ravi":"is a good boy","rohan":"is a good boy","kadu":"is a bad boy"}

myfunc(normal,*har,**kw)




# enumerate function
"""
list=["chpstick","frenchprice","manchuryan","palak pakoda"]


for index, item in enumerate(list):
    if index%2==0:
        print(f"jarvis plesse buy this{item}")

"""

# main function

# def myfunc(add):
#     return f"{add} is a good boy"
#
#
#
# def fuck(num1,num2):
#     return num1+num2+5
#
#
# if __name__ == '__main__':
#     ml = myfunc("het")
#     print(ml)
#     o = fuck(4, 5)
#     print(o)
#


lis="het","roha","vismay","jay","mango","kiko","ravi","kadu"
#
# for item in lis:
#     print(item,"and",end=" ")
#

#
# a=" and ".join(lis)
# print(a,"other fucker boys are in list")
#




