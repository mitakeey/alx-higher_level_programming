#!/usr/bin/python3
"""
This module implements a custom list object
"""


class MyList(list):
    
    def print_sorted(self):
        
        print(sorted(self))
