import sympy as sym
import numpy as np
import numba
import multiprocessing as mp
from ..src.PrimorialUtils import *


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

    primes_log3_list = np.log(np.log(range_primorials_log(mstart=mstart, mend=mend)))
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