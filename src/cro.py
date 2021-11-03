#!/usr/bin/python3

from src.coral import Coral
from src.health import Health
import numpy as npy
import random


class CRO(object):

    """class to describe all the logic of Coral Reef Optimization Algorithm"""

    def __init__(self, N=100, M=100, rho_zero=0.2, Fb=0.8, k=30, Fa=0.1, Fd=0.1):
        """
            CRO class constructor
        """
        # Tamaño de la parcela
        self.N = N
        self.M = M

        # Grado de libre/ocupado
        self.rho_zero = rho_zero

        # Grado de broadcast spawners
        self.Fb = Fb

        # Grado de Brooding
        self.Fbi = 1 - self.Fb

        # Numero de intentos de falledos de larvae setting
        self.k = k

        # Grado de reproducción asexual
        self.Fa = Fa

        # Grado de depredacción
        self.Fd = Fd

        # Iniciamos la función de salud de los corales :)
        self.fitness = Health(0.5, 0.5)

        # Iniciamos el arrecife
        self.reef = self.init_reef(self.N, self.M, self.rho_zero)

    def init_reef(self, N, M, rho_zero):
        """
            Metodo para inicializar el arrecife
        """
        reef = [None]*(M*N)

        # Vamos a rellenar siguiendo el parametro de rho_Zero
        n_init_corals = int(npy.round(M*N*rho_zero))

        # Vamos a generar el arrecife
        for i in range(0, n_init_corals):

            # En este punto habria que asegurarse que no generamos corales iguales en la inicialización...
            # Pero de momento para ganar en timepo de computo, vamos a obviarlo de momento...
            _id = Coral.getRandomID()
            reef[i] = Coral(_id, self.fitness.g(_id))

        # Hacemos un shuffleeeee
        random.shuffle(reef)

        return reef
