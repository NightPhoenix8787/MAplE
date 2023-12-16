import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "Maple",
    version = "1.0.0",
    author = "NightPhoenix",
    author_email="codenight8787@gmail.com",
    description="maple - a simple python maple library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NightPhoenix8787/Maple",                                         packages=setuptools.find_packages(),     
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )