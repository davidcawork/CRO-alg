#!/usr/bin/python3

from src.cro import CRO
import logging, os


if __name__ == '__main__':

    # Ponemos el nivel de log deseado
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

    # Path results
    pathRest = 'results'

    # Lets create the results directory
    if not os.path.exists(pathRest):
        os.makedirs(pathRest)

    # Numero de generaciones
    Ngens = 1000

    # Numero de repes
    Nruns = 100

    # COnfiguraciones a probar
    configs = {'1': {'alpha': 0.5, 'betha' : 0.5}, '2': {'alpha': 0.25, 'betha' : 0.75}, '3': {'alpha': 0.75, 'betha' : 0.25}, '4': {'alpha': 0.9, 'betha' : 0.1}, '5': {'alpha': 0.1, 'betha' : 0.9}}

    for key in configs:    
        
        # Almacenamos un historico con los datos
        hist = dict()

        if not os.path.exists(pathRest + '/alpha_' + str(configs[key]['alpha'] * 100) + '_betha_' + str(configs[key]['betha'] *100)):
            os.makedirs(pathRest + '/alpha_' + str(configs[key]['alpha'] * 100) + '_betha_' + str(configs[key]['betha'] * 100))

        for run in range(Nruns):

            logging.info('[+] Config  - Alpha ' + str(configs[key]['alpha'] *100) + ' - Betha ' + str(configs[key]['betha'] * 100) + ' | Run : '+ str(run))

            # Historico
            hist = dict()

            # Iniciamos el algoritmo
            CRO_obj = CRO(N=100, M=100, rho_zero=0.2, Fb=0.8, k=30, Fa=0.1, Fd=0.1, alpha = configs[key]['alpha'], betha = configs[key]['betha'])

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

                hist[str(i)] = { 'worse' : CRO_obj.getMinFitness(), 'avg' : CRO_obj.getAvgFitness(), 'best' : CRO_obj.getMaxFitness()}
                
                logging.info('Best-fitness: ' + str(round(CRO_obj.getMaxFitness(), 6)) + ' | Avg-fitness: ' + str(round(CRO_obj.getAvgFitness(), 6))+ ' | Worse-fitness: ' + str(round(CRO_obj.getMinFitness(), 6))+ ' | ('+str(round(i/Ngens*100, 2))+'% Completed) ')

            
            CRO_obj.write_historic(pathRest + '/alpha_' + str(configs[key]['alpha'] * 100) + '_betha_' + str(configs[key]['betha'] * 100) + '/hist_run_' + str(run), hist)
            CRO_obj.write_report(pathRest + '/alpha_' + str(configs[key]['alpha'] * 100) + '_betha_' + str(configs[key]['betha'] * 100) + '/hist_run_' + str(run))
        
        
    
    