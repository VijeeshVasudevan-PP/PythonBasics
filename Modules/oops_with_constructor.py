from inspect import AGEN_CLOSED
from logging import PlaceHolder


class sample:

    YEAR=2025
    def __init__(self,name,age,place):

        self.name= name
        self.age=age
        self.place=place


    def add_age(self):

        self.age=self.age+1


    def relocation(self):

        self.place=place

    def display(self):
        print(sample.YEAR)
        print(self.name)
        print(self.age)
        print(self.place)

name = ["vijeesh","tejaswi","tamasaa"]
place = ["vetom","purathur"]

objs1 = sample(name[0],39,place[0])

objs2 = sample(name[1],15,place[1])

objs1.display()
print("\n")
objs2.display()
print("\n")
print("\n")
print("------------------------------------------------------------")

sample.YEAR=sample.YEAR+1
objs1.add_age()
objs1.display()
print("\n")
objs2.add_age()
objs2.display()








