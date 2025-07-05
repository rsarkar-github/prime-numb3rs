import sympy as sym
import numpy as np


def sigma_by_n_upper_bound_func1(mstart:int, mend:int) -> np.ndarray:
    """
    Computes the upper bound on the ratio :math:`\sigma(n)/n` of a prime :math:`n = p_1^a_1 * ... * p_m ^ a_m`, with `m` distinct prime factors, 
    for :math:`mstart <= m <= mend`, where :math:`\sigma(n)` is the sum of divisors of `n`. The primes :math:`p_1, ... , p_m` and 
    exponents :math:`a_1, ..., a_m` are irrelevant to the calculation.

    The upper bound function 1: 

    .. math::
        \prod_{i=1}^{m} 1 / (1 - 1/q_i), 
    
    where q_i is the ith prime.

    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The np.ndarray of the upper bound on the ratio sigma(n)/n of for each primorial between primorial(mstart) and primorial(mend).
    """

    curr_prod = 1.0
    for i in range(mstart):
        next_prime = sym.nextprime(n=1, ith=i+1)
        curr_prod *= 1.0 / (1.0 - 1.0 / next_prime)
    
    ratio_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)
    ratio_list[0] = curr_prod

    for i in range(mend - mstart):
        next_prime = sym.nextprime(n=1, ith=i+mstart+1)
        curr_prod *= 1.0 / (1.0 - 1.0 / next_prime)
        ratio_list[i + 1] = curr_prod
    
    return ratio_list
