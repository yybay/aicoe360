import unittest
import pandas as pd
from valiant.fairness import stats

class Test_Stats(unittest.TestCase):

    def test_anova(self):

        df = pd.read_csv('data/test-statsmodel.csv', index_col=False)

        options = {"model":"accuracy ~ C(gender) * C(accent) + C(gender)",
            "ss_type": 2, "robust":"hc3", "test":"F", "anova_type":"main"}

        model = stats.anova.StatsModel(df, 'accuracy')

        model.anova(print_output=False, **options)

        exactly_equal = pd.read_parquet('data/anova_df.parquet', engine='pyarrow')

        with self.subTest("Check for customized model fitting"):
            self.assertEqual(model.model, "accuracy ~ C(gender) * C(accent) + C(gender)")

        with self.subTest("Check anova results"):
            self.assertTrue(model.anova_df.equals(exactly_equal))


if __name__ == '__main__':
    unittest.main(verbosity=2)
