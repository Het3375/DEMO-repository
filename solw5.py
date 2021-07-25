guess_name=int(input("what do you want to file lock or retriet?\n"))
if guess_name==1:
 select_file= int(input("which file are you locked harry prees 1,het prees2 or rohan press3\n"))



 if select_file==1:
    b=int(input("which condition are lock harrysfood press1 or harrygym prees 2\n"))
    if b==1:
        f=open("harryfood.txt","a")
        f.write(input())
        f.close()
    else:
        f=open("harrygym.txt","a")
        f.write(input())
        f.close()


 if select_file==2:
    b=int(input("which condition are lock hetsfood press1 or hetsgym prees 2\n"))
    if b==1:
        f=open("hetfood.txt","a")
        f.write(input())
        f.close()
    else:
        f=open("hetgym.txt","a")
        f.write(input())
        f.close()

 if select_file==3:
    b=int(input("which condition are lock rohansfood press1 or rohanssgym prees 2\n"))
    if b==1:
        f=open("rohanfood.txt","a")
        f.write(input())
        f.close()
    else:
        f=open("rohagym.txt","a")
        f.write(input())
        f.close()


##this file is retriet
elif guess_name==2:
 select_file = int(input("which file are you locked harry prees 1,het prees2 or rohan press3\n"))

 if select_file == 1:
  b = int(input("which condition are retrive harrysfood press1 or harrygym prees 2\n"))

  if b == 1:
    f = open("harryfood.txt")
    print(f.read())
    f.close()
  elif b == 2:
   f = open("harrygym.txt")
   print(f.read())
   f.close()

 if select_file == 2:
  b = int(input("which condition are retrive hetsfood press1 or hetsgym prees 2\n"))

  if b == 1:
    f = open("hetfood.txt")
    print(f.read())
    f.close()
  elif b == 2:
   f = open("hetgym.txt")
   print(f.read())
   f.close()

 if select_file == 3:
  b = int(input("which condition are retrive rohanfood press1 or rohangym prees 2\n"))

  if b == 1:
    f = open("rohanfood.txt")
    print(f.read())
    f.close()
  elif b == 2:
   f = open("rohagym.txt")
   print(f.read())
   f.close()








































