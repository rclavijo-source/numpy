Diaz will likely be Bayern’s biggest signing of the summer, but not their last. They remain committed to other attacking targets, with Musiala still at least four months away from playing again after suffering a broken leg in the recent Club World Cup, Serge Gnabry into the final year of his contract and having turned 30 this month and Coman’s future uncertain.

An agreement for Stuttgart striker Nick Woltemade remains unlikely, with two offers already rejected, but interest in RB Leipzig winger Xavi Simons remains. There is pending sale revenue, too. Winger Bryan Zaragoza and left-back Adam Aznou will be leaving in the near future, and there is Premier League interest in Joao Palhinha, whose move from Fulham last summer has not been a success.

For Liverpool, this is both a well-negotiated deal and a very timely agreement. Having already spent so heavily on Wirtz, Ekitike, Jeremie Frimpong and Milos Kerkez, a significant sale revenue has obvious value in PSR terms.

The Athletic has estimated Liverpool’s PSR profit on Diaz to be around £48million.

When combined with the £30m received from Leverkusen for Jarell Quansah, their £10m made on Caoimhin Kelleher by selling him to Brentford, the £8.4m fee from Real Madrid for Alexander-Arnold and the £3m paid for Nat Phillips by West Bromwich Albion, their transfer profit this summer more than offsets the new annual amortisation costs brought on board via the new signings, and will go a long way toward counterbalancing the wages paid to those recruits this season.

And that’s before even considering the wage savings that sales naturally bring about.

This doesn’t mean the transfer business at Anfield has finished for the current window. While they are well covered in terms of left-sided attackers, the news that Isak wishes to explore opportunities away from Newcastle this summer is likely to see Liverpool redouble their efforts to land the 25-year-old Sweden international.




"""
The `numpy.core` submodule exists solely for backward compatibility
purposes. The original `core` was renamed to `_core` and made private.
`numpy.core` will be removed in the future.
"""
from numpy import _core

from ._utils import _raise_warning


# We used to use `np.core._ufunc_reconstruct` to unpickle.
# This is unnecessary, but old pickles saved before 1.20 will be using it,
# and there is no reason to break loading them.
def _ufunc_reconstruct(module, name):
    # The `fromlist` kwarg is required to ensure that `mod` points to the
    # inner-most module rather than the parent package when module name is
    # nested. This makes it possible to pickle non-toplevel ufuncs such as
    # scipy.special.expit for instance.
    mod = __import__(module, fromlist=[name])
    return getattr(mod, name)


# force lazy-loading of submodules to ensure a warning is printed

__all__ = ["arrayprint", "defchararray", "_dtype_ctypes", "_dtype",  # noqa: F822
           "einsumfunc", "fromnumeric", "function_base", "getlimits",
           "_internal", "multiarray", "_multiarray_umath", "numeric",
           "numerictypes", "overrides", "records", "shape_base", "umath"]

def __getattr__(attr_name):
    attr = getattr(_core, attr_name)
    _raise_warning(attr_name)
    return attr
