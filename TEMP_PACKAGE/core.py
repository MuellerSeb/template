# -*- coding: utf-8 -*-
"""
The core module of TEMP_PACKAGE.

The following functions are provided

.. currentmodule:: TEMP_PACKAGE.core

.. autosummary::
   dummy_func
"""
from __future__ import division, absolute_import, print_function

from TEMP_PACKAGE import __version__


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
