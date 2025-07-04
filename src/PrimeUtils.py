import sympy as sym
import sympy.ntheory as nt
import numpy as np


def divisor_sum(n:int) -> int:
    return nt.divisor_sigma(n)

def divisor_sum_list(nlist:list) -> list:
    return [nt.divisor_sigma(n) for n in nlist]

def divisor_sum_by_n(n:int) -> float:
    return float(nt.divisor_sigma(n)) / n

def divisor_sum_by_n_list(nlist:list) -> list:
    return [float(nt.divisor_sigma(n)) / n for n in nlist]
