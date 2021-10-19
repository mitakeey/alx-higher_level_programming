#!/usr/bin/python3
"""
This module implements a Square object
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
   
    def __init__(self, size):
       
        super().__init__(size, size)
