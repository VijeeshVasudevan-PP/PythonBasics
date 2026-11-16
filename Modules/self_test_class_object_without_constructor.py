class sample():
    YEAR=2026
    def details(self):

        print("Enter Name")
        self.name=input()
        print("Enter age")
        self.age=int(input())
        print("Enter P;ace")
        self.place=input()

    def add_age(self):
        self.age=self.age+1

    def relocation(self):

        self.place=place

    def display(self):

        print("THE DETAILS")
        print("________________________________________")
        print(sample.YEAR)
        print(self.name)
        print(self.age)
        print(self.place)


objs1=sample()

objs1.details()
objs1.display()
objs2=sample()

objs2.details()

objs2.display()

print("After a year")
print("__________________________-")

sample.YEAR=sample.YEAR+1

objs1.add_age()
objs2.add_age()

objs1.display()
objs2.display()

