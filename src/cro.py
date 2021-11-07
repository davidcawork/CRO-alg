#!/usr/bin/python3

from src.coral import Coral
from src.health import Health
import numpy as npy
import random


class CRO(object):

    """class to describe all the logic of Coral Reef Optimization Algorithm"""

    def __init__(self, N=100, M=100, rho_zero=0.2, Fb=0.8, k=30, Fa=0.1, Fd=0.1, Pd = 0.02):
        """
            CRO class constructor
        """

        # Seed en uso
        self.seed = 0

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

        # Probabilidad de depredación
        self.Pd = Pd

        # Iniciamos la función de salud de los corales :)
        self.fitness = Health(0.5, 0.5)

        # Iniciamos el arrecife
        self.reef = self.init_reef(self.N, self.M, self.rho_zero)

        # Hacemos un seguimiento del ranking
        self.reef_ranking = self.updateRanking()

        # Colas de broadcast spawning, Brooding, sea
        self.act_queque = list()
        self.sea_queque = list()

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

    def updateRanking(self):
        """
            Metodo para actulizar el ranking
        """
        return sorted([a for a in self.reef if a is not None], key=lambda x: x.health, reverse=True)


    def getMaxFitness(self):
        """
            Metodo para obtener el mejor fitness
        """
        first = max(self.reef_ranking, key = lambda coral: coral.health)

        return first.health


    def getMinFitness(self):
        """
            Metodo para obtener el peor fitness
        """
        last = min(self.reef_ranking, key = lambda coral: coral.health)

        return last.health


    def getAvgFitness(self):
        """
            Metodo para obtener el fitness medio
        """
        avg = 0.0

        for coral in self.reef_ranking:
            avg += coral.health

        return avg/len(self.reef_ranking)

    def updateQueues(self):
        """
            Metodo para actualizar las colas
        """
        self.act_queque = [a for a in self.reef if a is not None]
        self.sea_queque = list()

    def BroadcastSpawning(self):
        """
            Metodo para definir el proceso de boradcast spawning
        """

        # Agitamos la lista y pillamos las Fb primeras
        random.shuffle(self.act_queque)

        # Vamos a iterar por todos los corales que vamos a emplear 
        n_broadcastSpawners = int(npy.round(self.Fb*len(self.act_queque)))

        # Hay que asegurarse que sean pares
        if n_broadcastSpawners % 2 != 0:
            n_broadcastSpawners-=1
        
        for j in range(0,int(n_broadcastSpawners/2)):
            parent_gen1, parent_gen2 = npy.array_split(self.act_queque[0].id, 2)
            mother_gen1, mother_gen2 = npy.array_split(self.act_queque[1].id, 2)

            # Vamos a tener en cuenta solo dos posibilidades de crossover
            if self.fitness.g(npy.concatenate((parent_gen1,mother_gen2))) > self.fitness.g(npy.concatenate((parent_gen2,mother_gen1))):
                self.sea_queque.append(Coral(npy.concatenate((parent_gen1,mother_gen2)), self.fitness.g(npy.concatenate((parent_gen1,mother_gen2)))))
            else:
                self.sea_queque.append(Coral(npy.concatenate((parent_gen2,mother_gen1)), self.fitness.g(npy.concatenate((parent_gen2,mother_gen1)))))

            # Nos quedamos con la mejor y eliminamos a los padres de la lista
            del self.act_queque[0:2]


    def Brooding(self):
        """
            Metodo para definir el proceso de Brooding
        """
        
        # Dado que suponemos que el proceso de Broadcast spawners siempre va antes..

        # Vamos a iterar por todos los corales restantes, que seran:
        n_Brooding = len(self.act_queque)

        for j in range(0, n_Brooding):
            
            # Hijo a mutar
            child_mut = npy.array_split(self.act_queque[0].id, 10)

            # Tiramos un numero random
            index_mut = random.randint(0,9)

            # Mutation 
            npy.random.shuffle(child_mut[index_mut])

            # Concatenate
            child_mutated = npy.concatenate(child_mut)

            # Add to the sea queque
            self.sea_queque.append(Coral(child_mutated, self.fitness.g(child_mutated)))

            # Remove it from act queque
            self.act_queque.pop()


    def LarvaeSetting(self):
        """
            Metodo para definir el proceso de LarvaeSetting
        """
        
        # Vamos a iterar por todas las larvas K veces
        for _larvae in range(0 , len(self.sea_queque)):
            for _try in range(0, self.k):
                
                # Elegir una casilla i,j de forma random
                _index = random.randint(0, (self.M * self.N) - 1)

                # Si hemos llegado al k tries 
                if _try == self.k:

                    # Tiramos la larva, no ha conseguido ser emplazada
                    self.sea_queque.pop()

                    # Pasamos a la siguiente 
                    break

                elif self.reef[_index] is None:
                    self.reef[_index] = self.sea_queque[0]

                    # Tiramos la larva ya que ha sido emplazada
                    self.sea_queque.pop()

                    break

                elif self.sea_queque[0].health > self.reef[_index].health:
                    self.reef[_index] = self.sea_queque[0]

                    # Tiramos la larva ya que ha sido emplazada
                    self.sea_queque.pop()

                    break



    def Depredation(self):
        """
            Metodo para definir el proceso de Depredation
        """

        # Hora de comeeeeee :D
        if random.uniform(0,1) < self.Pd:
            for j in range(0 , int(len(self.reef_ranking) * self.Fd)):
                self.reef[self.reef.index(self.reef_ranking[-j])] = None
 