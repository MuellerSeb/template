# -*- coding: utf-8 -*-
"""
The core module of YOUR_PACKAGE.

The following functions are provided

.. currentmodule:: YOUR_PACKAGE.core

.. autosummary::
   dummy_func
"""
from __future__ import division, absolute_import, print_function

from YOUR_PACKAGE import __version__


def dummy_func(dummy_arg=1, **kwargs):
    """
    A dummy function.

    Parameters
    ----------
    dummy_arg : TYPE, optional
        DESCRIPTION. The default is 1.
    **kwargs
        DESCRIPTION.

    Returns
    -------
    res : TYPE
        DESCRIPTION.

    """

    res = dummy_arg * __version__
    return res
