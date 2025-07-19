import sympy as sym
import numpy as np
import numba
import multiprocessing as mp
from src import PrimorialUtils as prim


def range_primorials_truncated_sum(mstart:int, mend:int, nproc:int=1) -> np.ndarray:
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
    
    nproc: int
        Number of processors to use for parallelization. Default is 1.

    Returns
    -------
    The np.ndarray of the truncated sum function for each primorial between primorial(mstart) and primorial(mend).
    """

    assert nproc >= 1
    numba.set_num_threads(n=min(nproc, mp.cpu_count()))

    primes_log3_list = np.log(np.log(prim.range_primorials_log(mstart=mstart, mend=mend)))
    result_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)
    m = [i for i in range(mstart, mend+1)]

    __truncated_sum_function_numba(input_arr=primes_log3_list, mlist=m, output_arr=result_list)
    
    return result_list


def range_primorials_truncated_sum_lower_bound_func1(mstart:int, mend:int, nproc:int=1) -> np.ndarray:
    """
    Computes a lower bound to the truncated sum function sum_{k=0}^{omega(n)} (ln ln ln (n))^k / k! for all the primorials, 
    primorial(m), for mstart <= m <= mend. Here omega(n)=m is the number of unique primes of n, 
    where n is the mth primorial prime given by n = p1 * p2 * ... * pm, and pk is the kth prime.

    The lower bound is obtained by setting n = 5040.
    ...

    Parameters
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.
    
    nproc: int
        Number of processors to use for parallelization. Default is 1.

    Returns
    -------
    The np.ndarray of the truncated sum function for each primorial between primorial(mstart) and primorial(mend).
    """

    assert nproc >= 1
    numba.set_num_threads(n=min(nproc, mp.cpu_count()))

    primes_log3_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64) * 0 + 5040
    primes_log3_list = np.log(np.log(np.log(primes_log3_list)))
    result_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)
    m = [i for i in range(mstart, mend+1)]

    __truncated_sum_function_numba(input_arr=primes_log3_list, mlist=m, output_arr=result_list)
    
    return result_list


@numba.njit(parallel=True)
def __truncated_sum_function_numba(input_arr:np.ndarray, mlist:list, output_arr:np.ndarray):
    """
    Computes the truncated sum function sum_{k=0}^{m} (ln ln ln (n))^k / k!.
    The shape of the input and output arrays must be same and must match size of mlist.
    ...

    Parameters
    ----------
    input_arr : np.ndarray
        The array of ln ln ln(n) values, of shape (m,).
    
    mlist : list
        The list of integer m values, of length m.
    
    output_arr : np.ndarray
        The array of truncated sums,  of shape (m,).
    
    Returns
    -------
    The np.ndarray of the truncated sum function for each element in the input array, where the summation happens for m terms given by mlist values.
    """

    assert (output_arr.shape == input_arr.shape) and (output_arr.shape[0] == len(mlist))

    m = len(mlist)
    for i in numba.prange(m):
        output_arr[i] = 1.0
        fac = 1.0
        for j in range(mlist[i]):
            fac *= input_arr[i] / (j + 1)
            output_arr[i] += fac


def range_primorials_truncated_sum_lower_bound_func2(mstart:int, mend:int, nproc:int=1) -> np.ndarray:
    """
    Computes a lower bound to the truncated sum function sum_{k=0}^{omega(n)} (ln ln ln (n))^k / k! for all the primorials, 
    primorial(m), for mstart <= m <= mend. Here omega(n)=m is the number of unique primes of n, 
    where n is the mth primorial prime given by n = p1 * p2 * ... * pm, and pk is the kth prime.

    The lower bound is obtained by only considering the leading order term in the sum and adding it to the value of the lower bound for the
    previous value of m. So recursively the lower bound is computed as follows:

    ..math::
        S(m) = sum_{k=0}^{m} (ln ln ln (n))^k / k!,
        S(k) = S(k-1) + (ln ln ln(n_k))^k / k!,
    
    where :math:`n_k = p1 * p2 * ... * pk`.
    ...

    Parameters.
    ----------
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.
    
    nproc: int
        Number of processors to use for parallelization. Default is 1.

    Returns
    -------
    The np.ndarray of the lower bound for the truncated sum function for each primorial between primorial(mstart) and primorial(mend).
    """

    assert nproc >= 1
    numba.set_num_threads(n=min(nproc, mp.cpu_count()))

    primes_log3_list = np.log(np.log(prim.range_primorials_log(mstart=mstart, mend=mend)))
    result_list = np.ndarray(shape=(mend - mstart + 1,), dtype=np.float64)
    m = [i for i in range(mstart, mend+1)]

    __truncated_sum_function_lower_bound_func2_numba(input_arr=primes_log3_list, mstart=mstart, mend=mend, output_arr=result_list)
    
    return result_list


@numba.njit
def __truncated_sum_function_lower_bound_func2_numba(input_arr:np.ndarray, mstart:int, mend:int, output_arr:np.ndarray):
    """
    Computes a lower bound to the truncated sum function sum_{k=0}^{omega(n)} (ln ln ln (n))^k / k! for all the primorials, given by lower bound func2.
    The shape of the input and output arrays must be same and must match size of mlist. Here omega(n)=m is the number of unique primes of n, 
    where n is the mth primorial prime given by n = p1 * p2 * ... * pm, and pk is the kth prime.

    The lower bound is obtained by only considering the leading order term in the sum and adding it to the value of the lower bound for the
    previous value of m. So recursively the lower bound is computed as follows:

    ..math::
        S(m) = sum_{k=0}^{m} (ln ln ln (n))^k / k!,
        S(k) = S(k-1) + (ln ln ln(n_k))^k / k!,
    
    where :math:`n_k = p1 * p2 * ... * pk`.
    ...

    Parameters
    ----------
    input_arr : np.ndarray
        The array of ln ln ln(n) values, of shape (m,).
    
    mstart : int
        The start value of m.
    
    mend : int
        The end value of m.
    
    output_arr : np.ndarray
        The array of truncated sums,  of shape (m,).
    
    Returns
    -------
    The np.ndarray of the lower bound for the truncated sum function for each primorial between primorial(mstart) and primorial(mend).
    """

    m = mend - mstart + 1
    assert (output_arr.shape == input_arr.shape) and (output_arr.shape[0] == m)
    
    # Compute the sum for S(mstart)
    fac = 1.0
    output_arr[0] = fac
    for j in range(mstart):
        fac *= input_arr[0] / (j + 1)
        output_arr[0] += fac

    # Compute the other terms
    for i in range(1, m):
        fac = 1.0
        for j in range(i + mstart):
            fac *= input_arr[i] / (j + 1)
        output_arr[i] = output_arr[i-1] + fac

    # for i in range(m):
    #     output_arr[i] = 1.0 + input_arr[i] + (input_arr[i] ** 2.0) / 2.0 + (input_arr[i] ** 3.0) / 6.0
