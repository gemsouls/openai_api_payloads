from setuptools import setup, find_packages

version = "1.0.0"
requirements = [
    "pydantic"
]


setup(
    name="auto_gptq",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=version,
    install_requires=requirements
)
