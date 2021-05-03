import setuptools
import os

ROOT_DIR = os.path.dirname(__file__)
REQUIREMENTS = [line.strip() for line in open(os.path.join(ROOT_DIR, "requirements.txt")).readlines()]

setuptools.setup(
    name="smallapp",
    version='0.0.0',
    packages=setuptools.find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=REQUIREMENTS,
)
