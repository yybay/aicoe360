"""
This module builds sampling strategies that ensures balanced sampling across important
key predictors, beyond the y-label.

For instance, for a classifier that has protected classes (e.g. gender) as predictors,
it is imperative that during the sampling process of train_test_split, there exists approximately
balanced numbers of males and females in both the train and test set, in order
for the model to be reliable, trustworthy, and devoid of potential biases.
"""

#pylint: disable=C0103

import pandas as pd
import numpy as np


class Balanced_sampling:
    """
    Implementation of balanced stratified random sampling from the population.
    """

    def __init__(self, df, dep_var):
        """
        Create an instance of the :class:`Balanced_sampling`

        :param df: dataframe of dataset with independent and dependent variables
        :type df: pandas.DataFrame
        :param dep_var: name of dependent variable column. All other variables in dataframe are assumed to be independent variables
        :type dep_var: string
        """

        self.df = df.copy()
        self.indep_var = [x for x in df.columns if dep_var not in x]
        self.dep_var = dep_var


    def stratified_random_sampler(self, dist, min_sample_size, stratified_col, balanced_col=None, write_output=True, **kwargs):
        """
        Produces a stratified random sample while keeping important features balanced

        :param dist: dataframe that contains two columns. First column contains the categories, and second column contains the numbers in each category
        :type dist: pandas.DataFrame
        :param min_sample_size: minimum desired sample size
        :type min_sample_size: int
        :param statified_col: name of the column to be stratified in df
        :type stratified_col: str
        :param balanced_col: name of the column to be balanced in df
        :type balanced_col: str, optional
        :param write_output: outputs an excel file with the sampled data. Default is True
        :type write_output: bool, optional
        :return: `pandas.DataFrame` with the stratified random sample
        """

        self.dist = dist
        self.min_sample_size = min_sample_size
        self.stratified_col = stratified_col
        self.balanced_col = balanced_col
        self.write_output = write_output
        _stratified_random_sampling(self, **kwargs)

        return self.df_stratified_random_sample


    def _stratified_random_sampling(self, **kwargs):
        return
