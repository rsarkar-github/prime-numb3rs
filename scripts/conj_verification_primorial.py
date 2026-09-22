from src.Constants import NtConstants
from src.PrimorialUtils import *
from src.GeneralUtils import *
from src.TruncatedSum import *
from matplotlib import pyplot as plt


if __name__ == "__main__":
    """
    This script contains codes for experiments for testing the conjecture for primorial primes.

    ----------
    Notation
    The ith prime is denoted as p_i.
    primorial(i) is the ith primorial number, obtained as p1 * ... * pi

    This compares the following functions:

    Function 1 (LHS):
    .. math:: 
        e^{-gamma} * sigma(primorial(m)) / primorial(m)
    
    Function 2 (LHS):
    .. math:: 
        prod_{i=1}^{m} e^{-gamma} * 1.0 / (1.0 - 1.0 / p_i)
    """

    # Initialize the class of constants
    consts = NtConstants()
    
    # Set m values, nproc
    mstart = 2
    mend = 1000
    nproc = 16

    mlist = np.arange(mstart, mend + 1, 1)
    # mlist = np.arange(mstart+1, mend + 1, 1)

    # Compute lhs of the conjecture
    lhs = range_primorials_sigma_by_n(mstart=mstart, mend=mend)
    lhs = lhs / consts.epowgamma

    # Compute upper bound on lhs of the conjecture
    lhs1 = sigma_by_n_upper_bound_func1(mstart=mstart, mend=mend)
    lhs1 = lhs1 / consts.epowgamma

    # Compute rhs of the conjecture
    # rhs = range_primorials_truncated_sum(mstart=mstart, mend=mend, nproc=nproc)
    # rhs1 = range_primorials_truncated_sum_lower_bound_func2(mstart=mstart, mend=mend, nproc=nproc)

    # rhs = range_primorials_truncated_sum(mstart=mstart, mend=mend+1, nproc=nproc)
    # rhs1 = range_primorials_truncated_sum(mstart=mstart, mend=mend-1, nproc=nproc)
    # rhs2 = range_primorials(mstart=mstart+1, mend=mend)

    # for i in range(0, mend-mstart):
    #     rhs1[i] *= (1.0 + 1.0 / rhs2[i])


    # rhs1 = range_primorials_truncated_sum_lower_bound_func1(mstart=mstart, mend=mend, nproc=nproc)

    # Plot the graphs
    plt.figure()
    plt.plot(mlist, lhs, '-r.')
    plt.plot(mlist, lhs1, '-k.')
    # plt.plot(mlist, rhs, '-b.')
    # plt.plot(mlist, rhs, '-g.')
    # plt.plot(mlist, rhs1, '-b.')
    plt.grid("on")
    plt.xlabel("$m$")
    # plt.legend(["lhs-exact", "lhs-ub", "rhs-exact", "rhs-lb"])
    # plt.legend(["lhs-exact", "rhs-exact", "rhs-lb"])
    # plt.legend(["$S_m$", "$S_{m-1} (q + 1)/q$"])
    plt.show()
