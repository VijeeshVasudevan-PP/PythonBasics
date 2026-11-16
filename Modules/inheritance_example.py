class sample:

    def __init__(self):
        print("saMPLEW CONSTRUCTOR")

    def set_name(self,name):

        self.name=name

        print("am sample classs!")










class hello(sample):


    def __init__(self):
        print("hello constructor")


    def set_name(self,name):

        super().set_name(name)
        print("hello set_name")





    def display_name(self):
        print(self.name)



class hello2(hello):

    def __init__(self):

        print("Hello 2 constructor")

        super().__init__()

    def wecome(self):

        print("Welcomr")





obj3=hello2()





