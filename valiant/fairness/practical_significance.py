"""
This module wraps metrics that measures individual and group fairness.

"""

#pylint: disable=C0103

import pandas as pd
import numpy as np


class Disparate_Impact:
    """
    The ratio of rate of favorable outcome for the minority group to that of the majority group.
    """

    def __init__(self, df):
        """
        Create an instance of the :class:`Disparate_Impact`

        :param pandas.DataFrame df: dataframe with independent and dependent variables
        """


    def four_fifths_rule(self, dep_var, ind_var, print_output=True, **kwargs):
        """
        The four-fifths or 80% rule is described by the guidelines as “a selection rate for any
        race, sex, or ethnic group which is less than four-fifths (or 80%) of the  rate for the
        group with the highest rate will generally be regarded by the Federal enforcement agencies
        as evidence of adverse impact, while a greater than four-fifths rate will generally not be
        regarded by Federal enforcement agencies as evidence of adverse impact.”

        Since the 80% test does not involve probability distributions to determine whether
        the disparity is a “beyond chance” occurrence, it is usually not regarded as a definitive
        test for adverse impact.

        Instead, other statistical tests may be used for this purpose.

        :param string dep_var: dependent variable name in dataframe
        :param string ind_var: independent variable name in dataframe
        :return:
            - ratio (:py:class:`float`) - the rate of favorable outcome for the minority group to that of the majority group
            - violation (:py:class:`boolean`) to indicate whether the four-fifths rule is violated. If True, ratio is < 80%.
        """

        cat = df[ind_var].unique()
        return


