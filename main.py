#!/usr/bin/python3

from src.cro import CRO
import logging


if __name__ == '__main__':

    # Ponemos el nivel de log deseado
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

    # Iniciamos el algoritmo
    CRO_obj = CRO(N=100, M=100, rho_zero=0.2, Fb=0.8, k=30, Fa=0.1, Fd=0.1)

    # Numero de generaciones
    Ngens = 1000

    # Iteramos para todas las generaciones
    for i in range(Ngens):

        # Update queues
        CRO_obj.updateQueues()

        # Upadte ranking
        CRO_obj.reef_ranking = CRO_obj.updateRanking()

        # Broadcast Spawning
        CRO_obj.BroadcastSpawning()

        # Brooding
        CRO_obj.Brooding()

        # Larvae Setting
        CRO_obj.LarvaeSetting()

        if i != Ngens:

            # Depredation
            CRO_obj.Depredation()


    
    