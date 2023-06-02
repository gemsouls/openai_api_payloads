from setuptools import setup, find_packages

from src.openai_api_payloads import __version__

requirements = [
    "pydantic"
]


setup(
    name="auto_gptq",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=__version__,
    install_requires=requirements,
    setup_requires=requirements
)
