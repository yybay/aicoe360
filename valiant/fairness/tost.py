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


class StatsModel:
    """
    Implementation of a suite of statistical models with automated checks for assumption
    violations
    """

    def __init__(self, df, dep_var):
        """
        Create an instance of the :class:`StatsModel`

        :param df: dataframe of dataset with independent and dependent variables
        :param dep_var: dependent variable string. All other variables in dataframe are assumed
         to be independent variables
        """

        self.df = df.copy()
        self.indep_var = [x for x in df.columns if dep_var not in x]
        self.dep_var = dep_var


    def tost(self, print_output=True, **kwargs):
        """
        The two-one-sided t-test is a test of (non-)equivalence for two independent samples

        TOST: two one-sided t tests

        null hypothesis: m1 - m2 < low or m1 - m2 > upp alternative hypothesis: low < m1 - m2 < upp

        where m1, m2 are the means, expected values of the two samples.

        If the pvalue is smaller than a threshold, say 0.05, then we reject the hypothesis that the difference between the two samples is larger than the the thresholds given by low and upp.


    	Parameters
    	----------
    	print_output : boolean
    	    Prints the dataframe results of the ANOVA analysis. Default is True.
    	low, upp : float
    	    Equivalence interval low < m1 - m2 < upp
    	usevar : str {'pooled' or 'unequal'}
    	    If 'pooled', then the standard deviation of the samples is assumed to be the same.
            If 'unequal', then Welsh ttest with Satterthwait degrees of freedom is used.
    	weights : tuple of None or ndarrays
            Case weights for the two samples. Default is None
    	transform : None or function
    	    If None (default), then the data is not transformed.
            Given a function, sample data and thresholds are transformed. If transform is log, then the equivalence interval is in ratio: low < m1 / m2 < upp

    	Returns
    	----------
        tost_df : dataframe
            pvalue (float): pvalue of the non-equivalence test
            t1, pv1 (tuple of floats): test statistic and pvalue for lower threshold test
            t2, pv2 (tuple of floats): test statistic and pvalue for upper threshold test
        """

        self.print_output = print_output
#        self.tost_df = self._tost_analysis(**kwargs)
#
#        return self.tost_df
#
#
#    def _tost_analysis(self, **kwargs):
#
#        # Farm out optional arguments
#        anova_type = kwargs.get("anova_type", "main")
#        self.model = kwargs.get("model", None)
#        scale = kwargs.get("scale", None)
#        test = kwargs.get("test", "F")
#        ss_type = kwargs.get("ss_type", 2)
#        robust = kwargs.get("robust", None)
#        cl = kwargs.get("cl", 0.05)
#
#        if anova_type == "main":
#            symbol = '+'
#        elif anova_type == "interaction":
#            symbol = '*'
#        else:
#            raise ValueError("Erroneous anova type: %s" %anova_type,
#                    " Choose \"main\" or \"interaction\"." )
#
#        # Defining model type
#        if self.model == None:
#            self.model = self.dep_var + ' ~ '
#            for i in range(len(self.indep_var)):
#                self.model = self.model + 'C(' + self.indep_var[i] + ')'
#
#                if i != len(self.indep_var)-1:
#                    self.model = self.model + symbol
#
#        # Ordinary least squares fit
#        self.ols_model = ols(self.model, self.df).fit()
#
#        # ANOVA
#        anova_df = sm.stats.anova_lm(self.ols_model, typ=ss_type, robust=robust, test=test, scale=scale)
#
#        if self.print_output==True: print(' ---------------\n', 'ANOVA analysis', '\n ---------------'),\
#                                    print(anova_df,'\n')
#
#        self._anova_assumptions(cl)
#
#        return anova_df
#
#
#    def _anova_assumptions(self, cl):
#        arrays = [['Normality (Shapiro-Wilk)', 'Normality (Shapiro-Wilk)', 'Variance', 'Variance'],
#                  ['test stats', 'p-value', 'test stats', 'p-value']]
#
#        temp = np.zeros((4, 1+len(self.indep_var)))
#
#        index = [self.dep_var]
#
#        # Experimental errors are normally distributed
#        temp[0,0], temp[1,0] = ss.shapiro(self.ols_model.resid)
#
#        if temp[1,0] > cl: # test for equal variances using Bartlett's test
#            for i in range(len(self.indep_var)):
#                index.append(self.indep_var[i])
#                list_unique = self.df[self.indep_var[i]].unique()
#                args = [self.df.loc[self.df[self.indep_var[i]]== x].accuracy for x in list_unique]
#                temp[2,i+1], temp[3,i+1] = ss.bartlett(*args)
#
#            arrays[0][2] = arrays[0][2] + ' (Bartlett)'
#            arrays[0][3] = arrays[0][3] + ' (Bartlett)'
#
#        else: # test for equal variances using Levene's test
#            for i in range(len(self.indep_var)):
#                list_unique = self.df[self.indep_var[i]].unique()
#                args = [self.df.loc[self.df[self.indep_var[i]]== x].accuracy for x in list_unique]
#                temp[2,i+1], temp[3,i+1] = ss.levene(*args)
#
#            arrays[0][2] = arrays[0][2] + ' (Levene)'
#            arrays[0][3] = arrays[0][3] + ' (Levene)'
#
#        self.anova_assump_df = pd.DataFrame(temp, index=arrays, columns=index)
#
#        if self.print_output==True: print(' ------------------\n', 'ANOVA assumptions', '\n ------------------'),\
#                                    print(self.anova_assump_df, '\n')
#        return
