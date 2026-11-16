class first:

    def display(self):

        print("First class")

class second:

    def display(self):

        print("second classs")

class third:

    def third_display(self):

        print("Third class")

class fourth(first,third,second):

    def final_display(self):
        print("Fourth class")


obj1=fourth()
print(fourth.mro())

# M R O  means method resolution order. 
