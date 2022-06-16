import numpy as np

class RandomTS:
    def __init__(self) -> None:
        self.__values: np.ndarray = []

    def generateTS(self)->np.ndarray:
        dt = 0.001
        horizon = np.arange(0,1,dt)
        frequencies = [50,120] #From Steven Bruntons example
        rndScaleFactor=2.5 #From Steven Bruntons example

        #Introducing periodicity
        LTrigo = lambda t : np.sin(2 * np.pi*frequencies[0]*t) + np.sin(2*np.pi*frequencies[1]*t)
        
        #Introducing randomness
        LRando = lambda: rndScaleFactor*np.random.rand()

        #Loop via list comprehension
        [self.__values.append(round(LTrigo(t)+LRando(),3)) for t in horizon]

        return np.array(self.__values)

    def __get_values(self)->np.ndarray:
        return  np.array(self.__values)

    tsValues = property(__get_values)