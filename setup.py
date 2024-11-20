from setuptools import setup, find_packages

setup(
    name="malekhoufel_weather_app",
    version="0.2.0",
    author="Malek",
    author_email="abdelmalek.houfel@sinay.fr",
    description="application météo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/malekhoufel/weatherApp.git",
    packages=find_packages(),
    install_requires=["requests"],
        
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
