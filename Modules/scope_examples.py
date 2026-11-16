def check_scope():

    def do_local():

        
        test = "Do Local Test"

    def do_non_local():
        test = "Do Non Local Test"

    def do_global():
        global test
        test = "Do Global Test"

    test = "Default"

    do_local()


    print(test)


check_scope()


