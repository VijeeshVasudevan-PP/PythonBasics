class sampleclass:


    def hello(self,detail):

        self.details=detail
        print(self.details)




#really we can see "self" in argmrent reciever in hello function.the objects objsc1 and objsc2 are really passed to "self"
Vijeesh = {"Name":"Vijeesh","Age":39,"Place":"Vettom"}

Tejawi = {"Name":"Tejaswi","Age":15,"Place":"Purathur"}

Tamasaa = {"Name":"Tamasaa","Age":11,"Place":"Purathur"}
objsc1 = sampleclass()

objsc1.hello(Vijeesh)




objsc2 = sampleclass()

objsc2.hello(Tejawi)


objsc3 = sampleclass()

objsc3.hello(Tamasaa)
