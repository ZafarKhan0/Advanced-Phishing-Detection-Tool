from setuptools import setup, find_packages

setup(
    name='AdvancedPhishingDetectionTool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ],
    entry_points={
        'console_scripts': [
            'phishing-detect=src.app:main'
        ]
    }
)
