

#This is to test the swaping formatte!


number1 = int(input("Enter 1st number for number1    : "))
number2 = int(input("Enter 2nd number for number2    : "))

tempnumber = number1

number1 = number2

number2 = tempnumber

#Below is the code to check the variable type .Its done by sending to a funcion "type" and
#sending the variable "tempnumber" as an argument

print(type(number1))

print("The swaped number is   "+"Number1 is  :   "+str(number1)+"   Number2 is :    "+str(number2))


print(type(number2))