from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rails-ar-encryption",
    version="0.0.1",
    author="ghn",
    description="Decrypts Rails payload.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["pycryptodome"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
