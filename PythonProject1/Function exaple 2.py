def hello(*details):
    print(details)

text = ["vijeesh","padiyam"]

value = 39

hello(text,value,48)

# DICTIONARY

names = {"name":"vijeesh","age":"39","place":"vettom"}

hello(names)
print(type(names))

#TUPLES

names = ("vijeesh",39,"padiyam")

hello(names)
print(type(names))

#SET

names = {"vijeesh",45,"vettom"}
hello(names)

print(type(names))