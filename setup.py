from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="procesamento de imagens",
    version="0.0.1",
    author="Murilo Calore",
    author_email="murilo.l.calore.r@gmail.com",
    description="short description for procesamento de imagens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mucarii/procesamento-de-imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)
