[![Python application](https://github.com/bjartejensen/airborne-fft-python/actions/workflows/airborne-fft-unittest.yml/badge.svg)](https://github.com/bjartejensen/airborne-fft-python/actions/workflows/airborne-fft-unittest.yml)

# Airborne-fft-python 

Airborne-fft-python is a sandbox restAPI exposing a small toolbox with some commonly use mathematical tools and techniques for data science.

## Fast Fourier Transform

Airborne-fft-python exhibit an attempt to implement [Steven L. Brunton's compact FFT application](https://www.youtube.com/watch?v=s2K1JfNR7Sc) which specifically applies to timeseries.

Our implementation make use of Numpy's Fast Fourier Transform package, `numpy.fft.fft` and `numpy.fft.ifft`. ([See documentation here](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html))

In short, the api allows the consumer to filter (denoise) noisy data (i.e. data associated with power spectrum density below a user given threshold) in order to capture the most prevalent periodicity in data.

