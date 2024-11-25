from setuptools import setup, find_packages

setup(
    name="retail_analysis",  # Package name
    version="1.0.0",  # Version number
    description="A package for analyzing the Sample Superstore dataset",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/retail_analysis",  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
