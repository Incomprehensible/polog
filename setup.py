from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "polog>=0.0.9", "vk-api>=11.9.1"]

setup(
    name="vk_polog_handler",
    version="0.0.9",
    author="Incomprehensible",
    author_email="bomanyte@student.21-school.ru",
    description="VK API-based handler for polog",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Incomprehensible/vk_polog_handler",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)