from ..src.Constants import NtConstants
from ..src.PrimorialUtils import *
from ..src.TruncatedSum import *
from matplotlib import pyplot as plt


if __name__ == "__main__":
    """
    This script contains codes for experiments for testing the conjecture for primorial primes.
    """

    # Initialize the class of constants
    consts = NtConstants()
    
    # Set m
    mstart = 2
    mend = 1000
    mlist = np.arange(mstart, mend + 1, 1)

    # Compute lhs of the conjecture
    lhs = range_primorials_sigma_by_n(mstart=mstart, mend=mend)
    lhs = lhs / consts.epowgamma

    # Compute rhs of the conjecture
    rhs = range_primorials_truncated_sum_function(mstart=mstart, mend=mend)

    # Plot the graphs
    plt.figure()
    plt.plot(mlist, lhs, '-r.')
    plt.plot(mlist, rhs, '-b.')
    plt.grid("on")
    plt.xlabel("m")
    plt.show()