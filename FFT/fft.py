import numpy as np

class FFTLocal:
    def __init__(self) -> None:
        pass

    def fft(self,data:np.ndarray):
        """
        Magnitude as lambda*lambda_conj = |lambda|^2 = a^2+b^2 where lambda = a+ib (complex) and lambda_conj a-i b
        (a+ib)*(a-ib)=a^2-(ib)^2=a^2+i^2*b^2=a^2-(-1)*b^2=a^2+b^2
        """
        self.__data = data
        fhat = np.fft.fft(data, data.size)
        self.__psd = (fhat*np.conj(fhat)/len(data)) #A vector of powers at each frequency
        self.__fftINV();
           
    def __filterPSD(self,psd:np.ndarray,minPct=0.0,maxPct=1.0)->np.ndarray:
        s=np.sort(np.unique(psd))
        min=200 #Currently hacked value s[-4]
        filteredPSD = np.where(psd > min, psd, 0)
        return filteredPSD

    def __fftINV(self):
        """
        Filtering the power spectrum density and applying inverse fft to get time values back
        """
        filteredFhat = self.__filterPSD(self.__psd)
        self.__periodicity = np.fft.ifft(filteredFhat).real

    def __get_psd(self)->np.ndarray:
        return self.__psd

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


