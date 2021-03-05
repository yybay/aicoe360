"""
This module implements the abstract base classes for all explain-specific implementations
"""


class Explain():
    """
    Abstract base class for all explain abstract base classes.
    """

#    explain_params: List[str] = list()

    def __init__(self, explainer):
        """
        :param explainer: An explain object.
        """

#    @property
#    def explainer(self):
#        return self._explainer
#
#    @property
#    def explainer_requirements(self):
#        return self._explainer_requirements
#
#    def set_params(self, **kwargs) -> None:
#        """
#        Take in a dictionary of parameters and apply explain-specific checks before saving them as attributes.
#        :param kwargs: A dictionary of explain-specific parameters.
#        """
#        for key, value in kwargs.items():
#            if key in self.explain_params:
#                setattr(self, key, value)
#        self._check_params()
#
#    def _check_params(self) -> None:
#        pass
