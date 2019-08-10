def cars():
    mylist = list()

    for index,i in enumerate(range(10)):
        mylist.append({"id":index,"name":"Car " + str(i)})

    return mylist
