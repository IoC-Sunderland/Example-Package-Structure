import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-4-IoC-Sunderland", # Replace with your own username
    version="0.0.1",
    author="Gav McClary",
    author_email="gavin.mcclary@sunderland.ac.uk",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IoC-Sunderland/Example-Package-Structure",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)