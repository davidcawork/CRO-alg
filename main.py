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

        # Broadcast Spawning
        CRO_obj.BroadcastSpawning()

        # Brooding
        CRO_obj.Brooding()

        # Larvae Setting
        CRO_obj.LarvaeSetting()

        if i != Ngens:

            # Upadte ranking
            CRO_obj.reef_ranking = CRO_obj.updateRanking()

            # Depredation
            CRO_obj.Depredation()

            # Upadte ranking
            CRO_obj.reef_ranking = CRO_obj.updateRanking()
        
        logging.info('Best-fitness: ' + str(round(CRO_obj.getMaxFitness(), 6)) + ' | Avg-fitness: ' + str(round(CRO_obj.getAvgFitness(), 6))+ ' | Worse-fitness: ' + str(round(CRO_obj.getMinFitness(), 6))+ ' | ('+str(round(i/Ngens*100, 2))+'% Completed) ')


        
        
    
    