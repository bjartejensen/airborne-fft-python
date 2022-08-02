import numpy as np

class FFT:
    def __init__(self) -> None:
        pass

    def fft(self,data:np.ndarray)->None:
        """
        Magnitude as lambda*lambda_conj = |lambda|^2 = (a+ib)*(a-ib)=a^2-(ib)^2=a^2+i^2*b^2=a^2-(-1)*b^2=a^2+b^2
        """
        self.__data = data
        fhat = np.fft.fft(data,data.size)
        self.__psd = (fhat*np.conj(fhat)/data.size) #A vector of powers at each frequency
        print("self.__psd",type(self.__psd[0]) ,self.__psd[:10])
        
        self.__fftINV();
           
    def __filterPSD(self,psd:np.ndarray,filterPct=0.75)->np.ndarray:

        maxPsd = self.psd.max()
        threshold=filterPct*maxPsd
        filteredPSD = np.where(psd > threshold, psd, 0)
        return filteredPSD

    def __fftINV(self):
        """
        Filtering the power spectrum density and applying inverse fft to get time values back
        """
        filteredFhat = self.__filterPSD(self.__psd)
        self.__periodicity = np.fft.ifft(filteredFhat).real

    #Getters to serve the exportable properties below

    @property
    def psd(self)->np.ndarray:
        #1. Take out negative frequencies and obs 0.
        #2. Only the real number. (Imaginary part is always zero.)
        return self.__psd[1: round(self.__data.size/2)].real 

    @property
    def original(self)->np.ndarray:
        return self.__data

    @property
    def periodicity(self)->np.ndarray:
        return self.__periodicity

    @property
    def noise(self)->np.ndarray:
        return self.__data - self.__periodicity



