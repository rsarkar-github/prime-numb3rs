import sympy as sym
import sympy.ntheory as nt
import numpy as np


def divisor_sum(n:int) -> int:
    r"""
    Computes the function :math:`\sigma(n)` for an input integer :math:`n`, where :math:`\sigma(n)` is the sum of divisors of :math:`n`.


    Parameters
    ----------
    n : int
        Input integer :math:`n`.

    Returns
    -------
    int
        The quantity :math:`\sigma(n)`.
    """
    return nt.divisor_sigma(n)


def divisor_sum_list(nlist:list) -> list:
    r"""
    Computes the function :math:`\sigma(n)` for each input integer :math:`n` in a list, where :math:`\sigma(n)` is the sum of divisors of :math:`n`.


    Parameters
    ----------
    n : list[int]
        Input list of integers.

    Returns
    -------
    list[int]
        The list of integers of the computed :math:`\sigma(n)` values for each :math:`n` in the input list.
    """
    return [nt.divisor_sigma(n) for n in nlist]


def divisor_sum_by_n(n:int) -> float:
    r"""
    Computes the function :math:`\sigma(n)/n` for an input integer :math:`n`, where :math:`\sigma(n)` is the sum of divisors of :math:`n`.


    Parameters
    ----------
    n : int
        Input integer :math:`n`.

    Returns
    -------
    int
        The quantity :math:`\sigma(n)/n`.
    """
    return float(nt.divisor_sigma(n)) / n


def divisor_sum_by_n_list(nlist:list) -> list:
    r"""
    Computes the function :math:`\sigma(n)/n` for each input integer :math:`n` in a list, where :math:`\sigma(n)` is the sum of divisors of :math:`n`.


    Parameters
    ----------
    n : list[int]
        Input list of integers.

    Returns
    -------
    list[int]
        The list of integers of the computed :math:`\sigma(n)/n` values for each :math:`n` in the input list.
    """
    return [float(nt.divisor_sigma(n)) / n for n in nlist]
