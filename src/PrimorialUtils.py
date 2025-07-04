import sympy as sym
import numpy as np


def primorial(m:int) -> int:
    """
    Computes the mth primorial prime.
    ...

    Parameters
    ----------
    m : int
        The value of m.

    Returns
    -------
    The mth primorial prime.
    """

    return sym.primorial(m)


def first_m_primorials(m:int) -> list:
    """
    Computes the first m primorial primes.
    ...

    Parameters
    ----------
    m : int
        The value of m.

    Returns
    -------
    The list of first m primorial primes.
    """

    primorial_list = []
    prime_prod_curr = 1

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        prime_prod_curr *= next_prime
        primorial_list.append(prime_prod_curr)
    
    return primorial_list


def first_m_primorials_log(m:int) -> np.ndarray:
    """
    Computes the logarithm (base e) of the first m primorial primes.
    ...

    Parameters
    ----------
    m : int
        The value of m.

    Returns
    -------
    The np.ndarray of logarithm (base e) of the first m primorial primes.
    """

    primorial_log_list = np.ndarray(shape=(m,), dtype=np.float64)
    curr_sum = 0.0

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        curr_sum += np.log(next_prime)
        primorial_log_list[i] = curr_sum
    
    return primorial_log_list


def range_primorials(mstart:int, mend:int) -> list:
    """
    Computes the primorials, primorial(m), for mstart <= m <= mend.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The list of the primorials between primorial(mstart) and primorial(mend).
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
    """
    Computes the logarithm (base e) of the primorials, primorial(m), for mstart <= m <= mend.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The np.ndarray of the logarithm (base e) for each primorial between primorial(mstart) and primorial(mend).
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
    """
    Computes the first m primes.
    ...

    Parameters
    ----------
    m : int
        The value of m.

    Returns
    -------
    The list of first m primes.
    """
    prime_list = []

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        prime_list.append(next_prime)
    
    return prime_list


def first_m_primes_log(m:int) -> np.ndarray:
    """
    Computes the logarithm (base e) of the first m primes.
    ...

    Parameters
    ----------
    m : int
        The value of m.

    Returns
    -------
    The np.ndarray of logarithm (base e) of the first m primes.
    """

    prime_log_list = np.ndarray(shape=(m,), dtype=np.float64)

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        prime_log_list[i] = np.log(next_prime)
    
    return prime_log_list


def range_primes(mstart:int, mend:int) -> list:
    """
    Computes the primes in the range prime(mstart) and prime(mend), where prime(k) is the kth prime.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The list the primes in the range prime(mstart) and prime(mend).
    """
    prime_list = []

    for i in range(mend - mstart + 1):
        next_prime = sym.nextprime(n=1, ith=i+mstart)
        prime_list.append(next_prime)
    
    return prime_list


def range_primes_log(mstart:int, mend:int) -> np.ndarray:
    """
    Computes the logarithm (base e) of all the primes in the range prime(mstart) and prime(mend), where prime(k) is the kth prime.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The np.ndarray of logarithm (base e) of all the primes in the range prime(mstart) and prime(mend).
    """
    prime_log_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)

    for i in range(mend - mstart + 1):
        next_prime = sym.nextprime(n=1, ith=i+mstart)
        prime_log_list[i] = np.log(next_prime)
    
    return prime_log_list


def first_m_primorials_sigma_by_n(m:int) -> np.ndarray:
    """
    Computes the ratio sigma(n)/n of the first m primorials, where sigma(n) is the sum of divisors of n.
    ...

    Parameters
    ----------
    m : int
        The value of m.

    Returns
    -------
    The np.ndarray of the ratio sigma(n)/n of the first m primorials.
    """

    ratio_list = np.ndarray(shape=(m,), dtype=np.float64)
    curr_prod = 1.0

    for i in range(m):
        next_prime = sym.nextprime(n=1, ith=i+1)
        curr_prod *= (1.0 + 1.0 / next_prime) 
        ratio_list[i] = curr_prod
    
    return ratio_list


def range_primorials_sigma_by_n(mstart:int, mend:int) -> np.ndarray:
    """
    Computes the ratio sigma(n)/n of the primorials, primorial(m), for mstart <= m <= mend., where sigma(n) is the sum of divisors of n.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.

    Returns
    -------
    The np.ndarray of the ratio sigma(n)/n of for each primorial between primorial(mstart) and primorial(mend).
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
