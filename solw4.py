print("which rows you can use?")
num1=int(input())
print("which value you can use? 0 or 1?")
new=bool (int(input()))



if new==0:
       for x in range(0,num1+1):
           print("*"* x )

elif new==1:
    for x in range(num1,0,-1):
        print("*" * x)

