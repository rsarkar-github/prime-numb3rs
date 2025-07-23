import sympy as sym
import numpy as np


def primorial(m:int) -> int:
    r"""
    Computes the :math:`m^{\mathrm{th}}` primorial prime :math:`p_1 p_2 ... p_m`, where :math:`p_k` is the :math:`k^{\mathrm{th}}` prime.

    Parameters
    ----------
    m : int
        The value of :math:`m`.

    Returns
    -------
    int
        The :math:`m^{\mathrm{th}}` primorial prime.
    """

    return sym.primorial(m)


def first_m_primorials(m:int) -> list:
    r"""
    Computes the first :math:`m` primorial primes. The :math:`m^{\mathrm{th}}` primorial prime is given by
    :math:`p_1 p_2 ... p_m`, where :math:`p_k` is the :math:`k^{\mathrm{th}}` prime.

    Parameters
    ----------
    m : int
        The value of :math:`m`.

    Returns
    -------
    list[int]
        The list of first :math:`m` primorial primes.
    """

    primorial_list = []
    prime_prod_curr = 1

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        prime_prod_curr *= next_prime
        primorial_list.append(prime_prod_curr)
    
    return primorial_list


def first_m_primorials_log(m:int) -> np.ndarray:
    r"""
    Computes the logarithm (base :math:`e`) of the first :math:`m` primorial primes. The :math:`m^{\mathrm{th}}` primorial prime is given by
    :math:`p_1 p_2 ... p_m`, where :math:`p_k` is the :math:`k^{\mathrm{th}}` prime.

    Parameters
    ----------
    m : int
        The value of :math:`m`.

    Returns
    -------
    np.ndarray
        The ndarray of logarithm (base :math:`e`) of the first :math:`m` primorial primes.
    """

    primorial_log_list = np.ndarray(shape=(m,), dtype=np.float64)
    curr_sum = 0.0

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        curr_sum += np.log(next_prime)
        primorial_log_list[i] = curr_sum
    
    return primorial_log_list


def range_primorials(mstart:int, mend:int) -> list:
    r"""
    Computes the primorials, :math:`\mathrm{primorial}(m)`, for :math:`\mathrm{mstart} \le m \le \mathrm{mend}`. The :math:`m^{\mathrm{th}}` primorial prime is given by
    :math:`p_1 p_2 ... p_m`, where :math:`p_k` is the :math:`k^{\mathrm{th}}` prime.

    Parameters
    ----------
    mstart : int
        The start value of :math:`m`.
    
    mend : int
        The end value of :math:`m`.

    Returns
    -------
    list[int]
        The list of the primorials between :math:`\mathrm{primorial(mstart)}` and :math:`\mathrm{primorial(mend)}`.
    """

    primorial_list = []
    primorial_mstart = sym.primorial(n=mstart)
    prime_prod_curr = primorial_mstart
    primorial_list.append(primorial_mstart)

    for i in range(mend - mstart):
        next_prime = sym.nextprime(n=1, ith=i+mstart+1)
        prime_prod_curr *= next_prime
        primorial_list.append(prime_prod_curr)
    
    return primorial_list


def range_primorials_log(mstart:int, mend:int) -> list:
    r"""
    Computes the logarithm (base :math:`e`) of the primorials, :math:`\mathrm{primorial}(m)`, for :math:`\mathrm{mstart} \le m \le \mathrm{mend}`.

    Parameters
    ----------
    mstart : int
        The start value of :math:`m`.
    
    mend : int
        The end value of :math:`m`.

    Returns
    -------
    np.ndarray
        The ndarray of the logarithm (base :math:`e`) for each primorial between :math:`\mathrm{primorial(mstart)}` and :math:`\mathrm{primorial(mend)}`.
    """

    primorial_log_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)
    primorial_mstart = sym.primorial(n=mstart)
    curr_sum = np.log(primorial_mstart)
    primorial_log_list[0] = curr_sum

    for i in range(mend - mstart):
        next_prime = sym.nextprime(n=1, ith=i+mstart+1)
        curr_sum += np.log(next_prime)
        primorial_log_list[i + 1] = curr_sum
    
    return primorial_log_list


def first_m_primes(m:int) -> list:
    r"""
    Computes the first :math:`m` primes.

    Parameters
    ----------
    m : int
        The value of :math:`m`.

    Returns
    -------
    list[int]
        The list of first :math:`m` primes.
    """
    prime_list = []

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        prime_list.append(next_prime)
    
    return prime_list


def first_m_primes_log(m:int) -> np.ndarray:
    r"""
    Computes the logarithm (base :math:`e`) of the first :math:`m` primes.

    Parameters
    ----------
    m : int
        The value of :math:`m`.

    Returns
    -------
    np.ndarray
        The ndarray of logarithm (base :math:`e`) of the first :math:`m` primes.
    """

    prime_log_list = np.ndarray(shape=(m,), dtype=np.float64)

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        prime_log_list[i] = np.log(next_prime)
    
    return prime_log_list


def range_primes(mstart:int, mend:int) -> list:
    r"""
    Computes the primes in the range :math:`\mathrm{prime(mstart)}` and :math:`\mathrm{prime(mend)}`, where :math:`\mathrm{prime}(k)` is the :math:`k^{\mathrm{th}}` prime.

    Parameters
    ----------
    mstart : int
        The start value of :math:`m`.
    
    mend : int
        The end value of :math:`m`.

    Returns
    -------
    list[int]
        The list the primes in the range :math:`\mathrm{prime(mstart)}` and :math:`\mathrm{prime(mend)}`.
    """
    prime_list = []

    for i in range(mend - mstart + 1):
        next_prime = sym.nextprime(n=1, ith=i+mstart)
        prime_list.append(next_prime)
    
    return prime_list


def range_primes_log(mstart:int, mend:int) -> np.ndarray:
    r"""
    Computes the logarithm (base :math:`e`) of all the primes in the range :math:`\mathrm{prime(mstart)}` and :math:`\mathrm{prime(mend)}`, where :math:`\mathrm{prime}(k)` is the :math:`k^{\mathrm{th}}` prime.

    Parameters
    ----------
    mstart : int
        The start value of :math:`m`.
    
    mend : int
        The end value of :math:`m`.

    Returns
    -------
    np.ndarray
        The ndarray of logarithm (base :math:`e`) of all the primes in the range :math:`\mathrm{prime(mstart)}` and :math:`\mathrm{prime(mend)}`.
    """
    prime_log_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)

    for i in range(mend - mstart + 1):
        next_prime = sym.nextprime(n=1, ith=i+mstart)
        prime_log_list[i] = np.log(next_prime)
    
    return prime_log_list


def first_m_primorials_sigma_by_n(m:int) -> np.ndarray:
    r"""
    Computes the ratio :math:`\sigma(n)/n` of the first :math:`m` primorials, where :math:`\sigma(n)` is the sum of divisors of :math:`n`.

    Parameters
    ----------
    m : int
        The value of :math:`m`.

    Returns
    -------
    np.ndarray
        The ndarray of the ratio :math:`\sigma(n)/n` of the first :math:`m` primorials.
    """

    ratio_list = np.ndarray(shape=(m,), dtype=np.float64)
    curr_prod = 1.0

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        curr_prod *= (1.0 + 1.0 / next_prime) 
        ratio_list[i] = curr_prod
    
    return ratio_list


def range_primorials_sigma_by_n(mstart:int, mend:int) -> np.ndarray:
    r"""
    Computes the ratio :math:`\sigma(n)/n` of the primorials, :math:`\mathrm{primorial}(m)`, for :math:`\mathrm{mstart} \le m \le \mathrm{mend}`, 
    where :math:`\sigma(n)` is the sum of divisors of :math:`n`.

    Parameters
    ----------
    mstart : int
        The start value of :math:`m`.
    
    mend : int
        The end value of :math:`m`.

    Returns
    -------
    np.ndarray
        The ndarray of the ratio :math:`\sigma(n)/n` for each primorial between :math:`\mathrm{primorial(mstart)}` and :math:`\mathrm{primorial(mend)}`.
    """

    curr_prod = 1.0
    for i in range(mstart):
        next_prime = sym.nextprime(n=1, ith=i+1)
        curr_prod *= 1.0 + 1.0 / next_prime 
    
    ratio_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)
    ratio_list[0] = curr_prod

    for i in range(mend - mstart):
        next_prime = sym.nextprime(n=1, ith=i+mstart+1)
        curr_prod *= 1.0 + 1.0 / next_prime
        ratio_list[i + 1] = curr_prod
    
    return ratio_list
