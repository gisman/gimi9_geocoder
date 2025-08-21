from setuptools import setup, find_packages

setup(
    name="gimi9-geocoder",
    version="0.1.0",
    author="gisman",
    author_email="gisman@gmail.com",
    description="A Python library for geocoding Korean addresses with integration for pandas.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gisman/gimi9_geocoder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "httpx",
        "pandas",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
)
