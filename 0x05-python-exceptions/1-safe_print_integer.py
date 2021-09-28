def safe_print_integer(value):

    while value > 0:
        try:
            print("{:d}".format(value) end="")
            return True
        except:
            print("Value is  not an integer")
            
