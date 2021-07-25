"""""
this is a calculator
print("choose num")
num1=int(input())


print("choose num")
num2=int(input())

# if num1==56 and num2==67:
#     print(567)
#

print("choose oprrator")
num3=input()
mystr = ["*", "+","/","-"]

if num1==56 and num2==9 and num3==mystr[1]:
    print(77)

elif num1==56 and num2==6 and num3==mystr[2]:
    print(4)


elif num1==45 and num2==3 and num3==mystr[0]:
    print(555)

elif num3==mystr[0]:
    print(num1*num2)

elif num3==mystr[1]:
    print(num1+num2)

elif num3==mystr[2]:
    print(num1/num2)

elif num3==mystr[3]:
    print(num1-num2)
"""""