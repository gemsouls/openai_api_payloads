from setuptools import setup, find_packages

version = "1.0.1"
requirements = [
    "pydantic"
]


setup(
    name="openai_api_payloads",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=version,
    install_requires=requirements
)
