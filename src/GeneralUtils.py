import sympy as sym
import numpy as np


def sigma_by_n_upper_bound_func1(mstart:int, mend:int) -> np.ndarray:
    """
    Computes the upper bound on the ratio :math:`\sigma(n)/n` of a prime :math:`n = {p_1}^{a_1}  ...  {p_m} ^ {a_m}`, with :math:`m` distinct prime factors, 
    for :math:`\text{mstart} <= m <= \text{mend}`, where :math:`\sigma(n)` is the sum of divisors of math:`n`. The primes :math:`p_1, ... , p_m` and 
    exponents :math:`a_1, ..., a_m` are irrelevant to the calculation.

    The upper bound function 1: 

    .. math::
        \prod_{i=1}^{m} 1 / (1 - 1/p_i), 
    
    where :math:`p_i` is the :math:`i ^ \text{th}` prime.

    ...

    Parameters
    ----------
    mstart : int
        The start value of math:`m`.
    
    mend : int
        The end value of math:`m`.

    Returns
    -------
    The np.ndarray of the upper bound on the ratio :math:`\sigma(n)/n` for each primorial between primorial(mstart) and primorial(mend).
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
