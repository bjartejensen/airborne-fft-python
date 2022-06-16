import numpy as np

class FFT:
    def __init__(self) -> None:
        pass

    def fft(self,data:np.ndarray):
        """
        Magnitude as lambda*lambda_conj = |lambda|^2 = (a+ib)*(a-ib)=a^2-(ib)^2=a^2+i^2*b^2=a^2-(-1)*b^2=a^2+b^2
        """
        self.__data = data
        fhat = np.fft.fft(data,data.size)
        self.__psd = (fhat*np.conj(fhat)/data.size) #A vector of powers at each frequency
        self.__fftINV();
           
    def __filterPSD(self,psd:np.ndarray,minPct=0.0,maxPct=1.0)->np.ndarray:
        #s=np.sort(np.unique(psd)) #s[-4]
        min=200 #Currently hacked value 
        filteredPSD = np.where(psd > min, psd, 0)
        return filteredPSD

    def __fftINV(self):
        """
        Filtering the power spectrum density and applying inverse fft to get time values back
        """
        filteredFhat = self.__filterPSD(self.__psd)
        self.__periodicity = np.fft.ifft(filteredFhat).real

    #Getters to serve the exportable properties below

    def __get_psd(self)->np.ndarray:

        #1. Take out negative frequencies and obs 0.
        #2. Only the real number. (Imaginary part is always zero.)
        return self.__psd[1: round(self.__data.size/2)].real 

    def __get_original(self)->np.ndarray:
        return self.__data

    def __get_periodicity(self)->np.ndarray:
        return self.__periodicity

    def __get_noise(self)->np.ndarray:
        return self.__data - self.__periodicity;

    psd = property(__get_psd)
    original = property(__get_original)
    periodicity = property(__get_periodicity)
    noise = property(__get_noise)


