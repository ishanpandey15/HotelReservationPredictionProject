from setuptools import setup,find_packages # type: ignore

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="HotelReservationPrediction",
    version="0.1",
    author="Ishan Pandey",
    packages=find_packages(),
    install_requires = requirements,
)