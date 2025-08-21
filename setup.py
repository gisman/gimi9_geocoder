from setuptools import setup, find_packages

setup(
    name="korean-geocoder",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for geocoding Korean addresses with integration for pandas.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/korean-geocoder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "fastapi",
        "uvicorn",
        "pandas",
        "pyproj",
        "pydantic",
        "httpx",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "gimi9-geocoder=gimi9_geocoder.client:main",
        ],
    },
)
