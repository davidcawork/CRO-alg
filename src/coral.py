#!/usr/bin/python3

import numpy as npy
from numpy import core


class Coral(object):

    """Class to emulate a Coral"""

    # Class macros
    MAX_ID_LEN = 100
    MAX_PLACED_STAs = 30

    def __init__(self, id, health):
        """
            Coral class constructor
        """
        self.id = id
        self.health = health

    @staticmethod
    def getRandomID():
        """
            Metodo para conseguir un ID random
        """
        # Zeros and ones props with max length of 100
        k = Coral.MAX_PLACED_STAs
        p = Coral.MAX_ID_LEN
        
        # Lets create the initial id
        arr = npy.array([1] * k + [0] * (p-k), dtype=npy.uint8)

        # Shuffleeeeeeeeeeeeee
        npy.random.shuffle(arr)

        return arr 
