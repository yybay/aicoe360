from setuptools import setup, find_packages

#with open('README.md') as readme_file:
#    README = readme_file.read()
#
#with open('HISTORY.md') as history_file:
#    HISTORY = history_file.read()

setup_args = dict(
    name='valiant',
    version='0.0.1',
    description='Useful tools to work with MDD analysis in Python',
#    long_description_content_type="text/markdown",
#    long_description=README + '\n\n' + HISTORY,
#    license='MIT',
    packages=find_packages(),
    author='Yong Yi Bay',
    author_email='yongyi.bay@wellsfargo.com',
    keywords=['AICOE', 'MDD', 'Explainability', 'fairness assessment', ],
    url='https://github.wellsfargo.com/NonApp-AdvancedAnalyticsLab/Valiant'
#    zip_safe=False,
#    download_url='https://pypi.org/project/elastictools/',
)

install_requires = [
    'numpy>=1.18.0'
#    'numpy>=1.18.0,<1.19.1'
#    'scipy>=1.4.0',
#    'pandas>=0.24.0',
#    'statsmodels>=0.10.0'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
