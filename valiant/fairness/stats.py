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

        :param df: dataframe of dataset with independent and dependent variables
        :type df: pandas dataframe
        :param dep_var: dependent variable string. All other variables in dataframe are assumed to be independent variables
        :type dep_var: string
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
            If `pooled`, then the standard deviation of the samples is assumed to be the same.
            If `unequal`, then Welsh ttest with Satterthwait degrees of freedom is used
        :type usevar: string, optional
        :param weights: Case weights for the two samples. Default is None
        :type weights: tuples of None or ndarrays, optional
        :param transform: \n
            - If `None` (default), then the data is not transformed \n
            - If given a `function`, sample data and thresholds are transformed. If transform is log, then the equivalence interval is in ratio: low < m1 / m2 < upp
        :type transform: None or function, optional
        :return: **Dataframe** with pvalue of equivalence test, test statistic and pvalue for lower/upper threshold test
        """

        self.print_output = print_output
#        self.tost_df = self._tost_analysis(**kwargs)
#
#        return self.tost_df


class Anova:
    """
    Implementation of a suite of statistical models with automated checks for assumption
    violations
    """

    def __init__(self, df, dep_var):
        """
        Create an instance of the :class:`Anova`

        :param df: dataframe of dataset with independent and dependent variables
        :type df: pandas dataframe
        :param dep_var: dependent variable string. All other variables in dataframe are assumed
         to be independent variables
        :type dep_var: string
        """

        self.df = df.copy()
        self.indep_var = [x for x in df.columns if dep_var not in x]
        self.dep_var = dep_var


    def anova(self, print_output=True, **kwargs):
        """
        Runs the anova analysis, as well as checking for model assumption violations

        :param print_output: Prints the dataframe results of the ANOVA analysis. Default is True.
        :type print_output: boolean, optional
    	:param scale: Estimate of variance, If `None`, will be estimated from the largest
    	    model. Default is `None`.
        :type scale: float
        :param test: {None, "F", "Chisq", "Cp"}. Test statistics to provide. Default is "F".
        :type test: string
        :param ss_type: {"I", "II", "III"} or {1, 2, 3}. The type of Anova test to perform. Default is `2`
        :type ss_type: string or int
        :param robust: {None, "hc0", "hc1", "hc2", "hc3"}.
            Use heteroscedasticity-corrected coefficient covariance matrix.
    	    If robust covariance is desired, it is recommended to use `hc3`.
        :type robust: string
        :return: **Dataframe** containing sum of squares, test statistic, and p-value
        """

        self.print_output = print_output
        self.anova_df = self._anova_analysis(**kwargs)

        return self.anova_df


    def _anova_analysis(self, **kwargs):

        # Farm out optional arguments
        anova_type = kwargs.get("anova_type", "main")
        self.model = kwargs.get("model", None)
        scale = kwargs.get("scale", None)
        test = kwargs.get("test", "F")
        ss_type = kwargs.get("ss_type", 2)
        robust = kwargs.get("robust", None)
        cl = kwargs.get("cl", 0.05)

        if anova_type == "main":
            symbol = '+'
        elif anova_type == "interaction":
            symbol = '*'
        else:
            raise ValueError("Erroneous anova type: %s" %anova_type,
                    " Choose \"main\" or \"interaction\"." )

        # Defining model type
        if self.model == None:
            self.model = self.dep_var + ' ~ '
            for i in range(len(self.indep_var)):
                self.model = self.model + 'C(' + self.indep_var[i] + ')'

                if i != len(self.indep_var)-1:
                    self.model = self.model + symbol

        # Ordinary least squares fit
        self.ols_model = ols(self.model, self.df).fit()

        # ANOVA
        anova_df = sm.stats.anova_lm(self.ols_model, typ=ss_type, robust=robust, test=test, scale=scale)

        if self.print_output==True: print(' ---------------\n', 'ANOVA analysis', '\n ---------------'),\
                                    print(anova_df,'\n')

        self._anova_assumptions(cl)

        return anova_df


    def _anova_assumptions(self, cl):
        arrays = [['Normality (Shapiro-Wilk)', 'Normality (Shapiro-Wilk)', 'Variance', 'Variance'],
                  ['test stats', 'p-value', 'test stats', 'p-value']]

        temp = np.zeros((4, 1+len(self.indep_var)))

        index = [self.dep_var]

        # Experimental errors are normally distributed
        temp[0,0], temp[1,0] = ss.shapiro(self.ols_model.resid)

        if temp[1,0] > cl: # test for equal variances using Bartlett's test
            for i in range(len(self.indep_var)):
                index.append(self.indep_var[i])
                list_unique = self.df[self.indep_var[i]].unique()
                args = [self.df.loc[self.df[self.indep_var[i]]== x].accuracy for x in list_unique]
                temp[2,i+1], temp[3,i+1] = ss.bartlett(*args)

            arrays[0][2] = arrays[0][2] + ' (Bartlett)'
            arrays[0][3] = arrays[0][3] + ' (Bartlett)'

        else: # test for equal variances using Levene's test
            for i in range(len(self.indep_var)):
                list_unique = self.df[self.indep_var[i]].unique()
                args = [self.df.loc[self.df[self.indep_var[i]]== x].accuracy for x in list_unique]
                temp[2,i+1], temp[3,i+1] = ss.levene(*args)

            arrays[0][2] = arrays[0][2] + ' (Levene)'
            arrays[0][3] = arrays[0][3] + ' (Levene)'

        self.anova_assump_df = pd.DataFrame(temp, index=arrays, columns=index)

        if self.print_output==True: print(' ------------------\n', 'ANOVA assumptions', '\n ------------------'),\
                                    print(self.anova_assump_df, '\n')
        return
