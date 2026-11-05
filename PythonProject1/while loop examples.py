print("Enter a number to see the multyplication Table")

number = int(input())

print("Enter the Tble to limit")

limit = int(input())

i=1

while i<=limit :

    print(str(number)+"x"+str(i)+"="+str(number*i))

    i=i+1

else :
    print("End of table!")

