import numpy as np
import pytest

# from Random.randomTs import RandomTS
from .randomTs import RandomTS


@pytest.fixture
def randomTs() -> np.ndarray:
    return RandomTS().tsValues


def test_for_empty_of_generateRandomTS(randomTs: np.ndarray) -> None:
    """Test if length of random series > 0"""
    assert len(randomTs) > 0


def test_for_length_of_generateRandomTS() -> None:
    """Test if length follows dt step size"""
    dt: float = 0.002
    rndTs: np.ndarray = RandomTS(dt).tsValues
    assert len(rndTs) == dt**-1.0
