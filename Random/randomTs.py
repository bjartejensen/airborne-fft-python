from unicodedata import decimal
import numpy as np


class RandomTS:
    def __init__(self, dt: decimal = 0.001) -> None:
        self.__values: np.ndarray = []
        self.__dt: decimal = dt
        self.__generateRandomTS()

    def __generateRandomTS(self) -> None:
        horizon = np.arange(0, 1, self.__dt)
        frequencies = [50, 120]
        rndScaleFactor = 2.5

        # Introducing periodicity
        def LTrigo(t: float) -> float:
            return np.sin(2 * np.pi*frequencies[0]*t) + np.sin(2*np.pi*frequencies[1]*t)

        # Introducing randomness
        def LRando() -> float:
            return rndScaleFactor*np.random.rand()

        # Loop via list comprehension
        self.__values = np.array([round(LTrigo(t)+LRando(), 3) for t in horizon])

    @property
    def tsValues(self) -> np.ndarray:
        return np.array(self.__values)
