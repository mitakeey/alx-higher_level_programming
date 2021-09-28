#!/usr/bin/python3
def safe_print_integer(value):

        while value > 0:
        try:
            print("{:d}".format(value) end="")
            return True
        except(ValueError, TypeError):
            return False
            
