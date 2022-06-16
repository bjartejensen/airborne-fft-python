
import numpy as np
#from scipy import rand

class Brunton:
    def __init__(self) -> None:
        pass
        self.__values: np.ndarray = []

    def generateRandomnessTS(self)->list:
        dt = 0.001
        horizon = np.arange(0,1,dt)
        frequencies = [50,120]
        rndScaleFactor=2.5

        LTrigo = lambda t : np.sin(2 * np.pi*frequencies[0]*t) + np.sin(2*np.pi*frequencies[1]*t)
        LRando = lambda: rndScaleFactor*np.random.rand()
        
        bruntonTs:list = []

        for t in horizon:
            value = round(LTrigo(t)+LRando(),3)
            self.__values.append(value)
            bruntonTs.append( {'time': t, 'value': value})

        return np.array(self.__values)

    def __get_values(self)->np.ndarray:
        return  np.array(self.__values)

    tsValues = property(__get_values)
        



