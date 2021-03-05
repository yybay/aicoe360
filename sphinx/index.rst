.. Valiant documentation master file, created by
   sphinx-quickstart on Thu Nov 19 17:08:46 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Validation Analysis Toolkit!
===========================================

Validation Analysis Toolkit (VALIANT) is a Python library for model validation purposes. VALIANT provides tools that enable
developers and researchers to evaluate, defend, certify and verify Machine Learning models and applications through explainability,
fairness assessments, and also against adversarial threats. VALIANT supports all popular machine learning
frameworks (TensorFlow, Keras, PyTorch, MXNet, scikit-learn, XGBoost, LightGBM, CatBoost, GPy, etc.), all data types
(images, tables, audio, video, etc.) and machine learning tasks (classification, object detection, generation,
certification, etc.).

..
    image:: ./images/adversarial_threats_attacker.png
  :width: 400
  :alt: ART Logo
  :align: center
..
    image:: ./images/adversarial_threats_art.png
  :width: 400
  :alt: ART Logo
  :align: center

The code of VALIANT is on `GitHub`_ and the Wiki contains overviews of implemented explainability, fairness, and sensitivity assessments.

The library is under continuous development. Feedback, bug reports and contributions are very welcome!

Supported Machine Learning Libraries
------------------------------------

* TensorFlow (v1 and v2) (https://www.tensorflow.org)
* Keras (https://www.keras.io)
* PyTorch (https://www.pytorch.org)
* MXNet (https://mxnet.apache.org)
* Scikit-learn (https://www.scikit-learn.org)
* XGBoost (https://www.xgboost.ai)
* LightGBM (https://lightgbm.readthedocs.io)
* CatBoost (https://www.catboost.ai)
* GPy (https://sheffieldml.github.io/GPy/)

.. toctree::
   :maxdepth: 2
   :caption: Modules

   modules/fairness
   modules/fairness/samplers
   modules/fairness/statistical_significance
   modules/fairness/practical_significance
   modules/fairness/combine_significance
   modules/explain
   modules/explain/knowledge_distillation


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Github: https://github.wellsfargo.com/NonApp-AdvancedAnalyticsLab/Valiant
