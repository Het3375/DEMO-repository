
"""""

#diconory,sets,for and while loops;


#dictionery syntax


thisdict={
    "gender":"male" ,
    "exam":"sem2",
    "total marks":"300",
    "highest marks in sem2 is":"267"
}
print(thisdict)

# "nested dictionerys"
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
 }
print(myfamily)

dift={
    "name":"het",
    "age":"21",
    "surname":"patel",

}
#

#.get is a enter for the dict
x=myfamily.get("child1")
print(x)


# .keys is a keywored
x=dift.keys()
print(x)


#add dob
dift["dob"]="14/12/2000"

print(x)


#change the val
dift.update({"surname":"sigh"})
dift ["surname"]="sigh"
print(dift)


#remove value

dift.pop("surname")
dift.popitem()
del dift
dift.items()   #all items show after this keywored
print(dift)

#copy keys in dictionery
mydr=dift.copy()
print(mydr)
"""""