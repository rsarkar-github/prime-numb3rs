from src.Constants import NtConstants
from src.PrimorialUtils import *
from src.GeneralUtils import *
from src.TruncatedSum import *
from matplotlib import pyplot as plt


def check_bounds(mstart=1, mend=100, nproc=1):

    # Initialize the class of constants
    consts = NtConstants()

    # Compute upper bound on lhs of the conjecture
    lhs_ub = sigma_by_n_upper_bound_func1(mstart=mstart, mend=mend)

    # Compute rhs
    rhs = range_primorials_truncated_sum_lower_bound_func1(mstart=mstart, mend=mend, nval=1.5e8, nproc=nproc)
    rhs *= consts.epowgamma

    # Print and write to file
    count = 0
    for k in range(mstart, mend+1):
        print("k = ", k, ", lhs = ", lhs_ub[count], ", rhs = ", rhs[count])
        count += 1


if __name__ == "__main__":
    
    check_bounds(mstart=1, mend=6, nproc=1)