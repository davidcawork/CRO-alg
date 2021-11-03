#!/usr/bin/python3

from src.cro import CRO
import logging


if __name__ == '__main__':

    # Ponemos el nivel de log deseado
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

    # Iniciamos el algoritmo
    CRO_obj = CRO(N=100, M=100, rho_zero=0.2, Fb=0.8, k=30, Fa=0.1, Fd=0.1)