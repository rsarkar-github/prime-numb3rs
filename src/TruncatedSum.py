import sympy as sym
import numpy as np
from ..src.PrimorialUtils import *


def range_primorials_truncated_sum_function(mstart:int, mend:int) -> np.ndarray:
    """
    Computes the truncated sum function sum_{k=0}^{omega(n)} (ln ln ln (n))^k / k! for all the primorials, primorial(m), for mstart <= m <= mend.
    Here omega(n)=m is the number of unique primes of n, where n is the mth primorial prime given by n = p1 * p2 * ... * pm, and pk is the kth prime.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The np.ndarray of the truncated sum function for each primorial between primorial(mstart) and primorial(mend).
    """

    primes_log3_list = np.log(np.log(range_primorials_log(mstart=mstart, mend=mend)))
    m = mend - mstart + 1

    result_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64) + 1.0
    fac = 1.0
    for i in range(mend):
        fac *= 1.0 / (i + 1)
        for j in range(max(0, i - mstart + 1), m):
            result_list[j] += fac * (primes_log3_list[j] ** (i + 1))
    
    return result_list
