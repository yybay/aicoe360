"""
Knowledge distillation - approaches that learn a simpler model based on a
complex model’s predictions. These simpler models can be considered as global
interpretations that are learned using a post-hoc surrogate model.

Papers:

- `L. J. Ba and R. Caurana. Do deep nets really need to be deep? CoRR, abs/1312.6184, 2013. <https://arxiv.org/abs/1312.6184>`_
- `C. Bucilua, R. Caruana, and A. Niculescu-Mizil. Model compression. In ˇ Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2006. <https://dl.acm.org/doi/pdf/10.1145/1150402.1150464?casa_token=AqdcozJZqVoAAAAA:rgn3A-yAhlSJ53bVyvx4FCV0dfoJdYE6BWMVFDWXqZlGQ-7llsdAp_aAwBZd3I3nlXifhYAf4b2n>`_
"""

#pylint: disable=C0103

import pandas as pd
import numpy as np


class Lgbm:
    """
    The ratio of rate of favorable outcome for the minority group to that of the majority group.
    """

    def __init__(self, df, label_name):
        """
        Create an instance of the :class:`Lgbm`

        :param pandas.DataFrame df: dataframe with independent and dependent variables
        :param string label_name: label name in dataframe. This refers to the complex model's predictions that the surrogate model is learning from.
        """

        self.df = df.copy()
        self.indep_var = [x for x in df.columns if dep_var not in x]
        self.dep_var = dep_var


    def surrogate_model(self, save_model=False, **kwargs):
        """
        Creates a surrogate model using the complex model's predictions.

        :param save_model: save the trained booster model using pickle. Default is False
        :type write_output: boolean, optional
        :return: booster - the trained booster model using LightGBM
        """

        return


