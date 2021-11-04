#!/usr/bin/python3

from src.coral import Coral
import scipy.io as sio
import numpy as npy
import math


class Health(object):

    """Class to work around Health func"""

    def __init__(self, alpha=0.5, betha=0.5, dataPath="src/data/data.mat"):
        """
            Constructor de la clase Health
        """
        self.alpha = alpha
        self.betha = betha
        self.dataPath = dataPath
        self.xp, self.C, self.bt = Health.loadData(self.dataPath)
        self.users = self.countUsers()

    @staticmethod
    def loadData(path):
        """
            FUncion para cargar el *.mat de datos
        """
        matData = sio.loadmat(path)
        return matData['xp'], matData['C'], matData['bt']

    @staticmethod
    def distance(x_1, y_1, x_2, y_2):
        """
            Metodo estatico para calcular la distancia euclidia entre dos puntos
        """
        return math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))

    def countUsers(self):
        """
            Metodo para pre-calcular usuarios por antena
        """
        arr = npy.zeros(Coral.MAX_ID_LEN, dtype=npy.int)

        for sta in self.bt:
            for user in self.xp:
                if Health.distance(sta[0], sta[1], user[0], user[1]) < 0.350:
                    i, j = npy.where(self.bt == sta)
                    arr[i[0]] += 1
        return arr

    def g(self, id):
        """
            Funcion de coste de la practica
        """
        index_sta = npy.where(id == 1)

        C1 = npy.sum(self.users[index_sta])
        C2 = npy.sum(self.C[index_sta])

        return self.alpha * C1 + self.betha * (1/C2)

