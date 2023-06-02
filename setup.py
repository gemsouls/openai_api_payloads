from setuptools import setup, find_packages

requirements = [
    "pydantic"
]


setup(
    name="auto_gptq",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version="1.0.0",
    install_requires=requirements
)
