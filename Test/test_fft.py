import numpy as np
import pytest

from unicodedata import decimal
from FFT.fft import FFT
from RandomTS.randomTs import RandomTS

@pytest.fixture
def randomTs()->np.ndarray:
    return RandomTS().tsValues

def test_for_return_type_fft(randomTs:np.ndarray)->None:
    """Test if length of random series > 0"""

    inst:FFT = FFT()
    inst.fft(randomTs)

    assert type(inst.periodicity[0])!=np.complex128
    assert type(inst.periodicity[0])==np.float64
    
   
def test_for_length_of_properties()->None:
    """Test if length follows dt step size"""

    dt:decimal=0.001    
    inst:FFT = FFT()
    inst.fft(RandomTS(dt).tsValues)

    expected_len:int =(dt**-1)

    assert len(inst.noise) == expected_len
    assert len(inst.original) == expected_len
    assert len(inst.periodicity) == expected_len
    assert len(inst.psd) == (dt**-1)/2 -1