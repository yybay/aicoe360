"""
This module implements the abstract base classes for all fairness-specific implementations
"""


class Fair():
    """
    Abstract base class for all fairness abstract base classes.
    """

    def __init__(self, fair):
        """
        :param fair: An fairness object.
        """
