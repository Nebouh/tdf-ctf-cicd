from setuptools import setup, find_packages

setup(
    name='pyyaml',
    version='6.0.1',
    packages=find_packages(),
    install_requires=[],  # Si tu veux ajouter des dépendances
    entry_points={
        'console_scripts': [
            'yaml = yaml.main:main',  # yaml sera la commande qui déclenchera ton script
        ],
    },
)
