class sample:

    YEAR=2025

    def __init__(self,name,age,place):

        self.name=name
        self.age=age
        self.place=place






    def add_age(self):
        self.age=self.age+1

    def relocation(self):

        self.place=place

    def display(self):

        print("Here are the details")
        print("\n")
        print("______________________________________________")
        print("\n")
        print(sample.YEAR)
        print(self.name)
        print(self.age)
        print(self.place)


    @classmethod
    def add_year(cls):

        sample.YEAR=sample.YEAR+1


    @staticmethod
    def display_ordinary():
        print("WELCOME ALL")






objs1=sample("vijeesh",39,"vettom")

objs2=sample("tejaswi",15,"purathur")
objs1.display()
objs2.display()

sample.add_year()

objs1.display()
objs2.display()

sample.display_ordinary()








