"""
This module wraps statistical modules and automatically delivers the p-value, test statistic,
with its associated model assumptions.
"""

#pylint: disable=C0103

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as ss
import numpy as np


class Tost:
    """
    Implementation of TOST with automated checks for assumption
    violations
    """

    def __init__(self, df, dep_var):
        """
        Create an instance of the :class:`Tost`

        :param pandas.DataFrame df: dataframe with independent and dependent variables
        :param string dep_var: name of dependent variable column. All other variables in dataframe are assumed to be independent variables
        """

        self.df = df.copy()
        self.indep_var = [x for x in df.columns if dep_var not in x]
        self.dep_var = dep_var


    def tost(self, low, upp, print_output=True, **kwargs):
        """
        The two-one-sided t-test is a test of (non-)equivalence for two independent samples

        TOST: two one-sided t tests

        null hypothesis: m1 - m2 < low or m1 - m2 > upp alternative hypothesis: low < m1 - m2 < upp

        where m1, m2 are the means, expected values of the two samples.

        If the pvalue is smaller than a threshold, say 0.05, then we reject the hypothesis that the difference between the two samples is larger than the the thresholds given by low and upp.

        :param low: Equivalence interval low < m1 - m2 < upp
        :type low: float
        :param upp: Equivalence interval low < m1 - m2 < upp
        :type upp: float
        :param print_output: Prints the dataframe results of the ANOVA analysis. Default is True
        :type print_output: boolean, optional
        :param usevar: {"pooled", "unequal"}
            - If `pooled`, then the standard deviation of the samples is assumed to be the same
            - If `unequal`, then Welsh ttest with Satterthwait degrees of freedom is used
        :type usevar: string, optional
        :param weights: Case weights for the two samples. Default is None
        :type weights: tuples of None or ndarrays, optional
        :param transform:
            - If `None` (default), then the data is not transformed
            - If given a `function`, sample data and thresholds are transformed. If transform is log, then the equivalence interval is in ratio: low < m1 / m2 < upp
        :type transform: None or function, optional
        :return: `pandas.DataFrame` with pvalue of equivalence test, test statistic and pvalue for lower/upper threshold test
        """

        self.print_output = print_output
#        self.tost_df = self._tost_analysis(**kwargs)
#
#        return self.tost_df
