
"""local variables and globel variables
x=6
def func():
    x=5
    x=5+6
    # global x
    x=x+6
    print(x)



func()
"""




# nested globel and local variables

x=100
def het():
    x=89

    def rohan():
      global x
      x=67
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)
het()





