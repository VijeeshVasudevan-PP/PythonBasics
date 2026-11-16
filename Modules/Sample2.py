def greatOrLess(value):
    if value < 0:
        print("The number is Negative")

    elif value > 0:
        print("The number is Possitive")

    else:
        print("The number is Zero")


def primary(number):
    flag=0

    if number<2:
        print("Number less than 2 is not considered as prime")




    for x in range(2,number-1):

        if number%x==0:

            flag=1
            break
    if flag==1:

        print("the number is NOT prime")

    else:
        print("The number id Prime")


