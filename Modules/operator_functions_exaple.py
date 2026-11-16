class sample:

    def set_name(self,name):

        self.name=name

    def __add__(self, other):

        fullname=self.name+"   "+other.name
        return fullname




obj1=sample()

obj2=sample()

obj1.set_name("vijeesh")
obj2.set_name("vasudevan")

full_name=obj1+obj2
print(full_name)

