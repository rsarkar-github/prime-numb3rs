from src.Constants import NtConstants
from src.PrimorialUtils import *
from src.GeneralUtils import *
from src.TruncatedSum import *
from matplotlib import pyplot as plt


if __name__ == "__main__":
    """
    This script contains codes for experiments for testing the conjecture for primorial primes.
    """

    # Initialize the class of constants
    consts = NtConstants()
    
    # Set m values, nproc
    mstart = 2
    mend = 100
    nproc = 16

    mlist = np.arange(mstart, mend + 1, 1)

    # Compute lhs of the conjecture
    lhs = range_primorials_sigma_by_n(mstart=mstart, mend=mend)
    lhs = lhs / consts.epowgamma

    lhs1 = sigma_by_n_upper_bound_func1(mstart=mstart, mend=mend)
    lhs1 = lhs1 / consts.epowgamma

    # Compute rhs of the conjecture
    rhs = range_primorials_truncated_sum(mstart=mstart, mend=mend, nproc=nproc)
    rhs1 = range_primorials_truncated_sum_lower_bound_func1(mstart=mstart, mend=mend, nproc=nproc)

    # Plot the graphs
    plt.figure()
    plt.plot(mlist, lhs, '-r.')
    plt.plot(mlist, lhs1, '-k.')
    plt.plot(mlist, rhs, '-b.')
    plt.plot(mlist, rhs1, '-g.')
    plt.grid("on")
    plt.xlabel("m")
    plt.legend(["lhs-exact", "lhs-ub", "rhs-exact", "rhs-lb"])
    plt.show()
