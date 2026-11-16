# This programme is to understand the basics of primary number chewcks


def primaryCall(value):
    flag=0
    for x in range(2,value-1):

        if value % x ==0:
            flag=1
            break
    if flag==1:

        print("The number is NOT PRIME")

    else:
        print("The number is PRIME")



def primary(num):

    if num<2:

        print("The number less than 2 NOT CONSIDERED AS PRIME")

    else:
        primaryCall(num)


