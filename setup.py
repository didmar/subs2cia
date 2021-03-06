import setuptools
from subs2cia import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subs2cia",
    version=__version__,
    license='MIT',
    author="Daniel Xing",
    author_email="danielxing97@gmail.com",
    description="A subtitle-based multimedia extractor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dxing97/subs2cia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        # create a cli command called 'subs2cia' which runs the main() function in subs2cia.cli
        'console_scripts': ['subs2cia=subs2cia.cli:main', 'subzipper=subs2cia.cli:subzipper_main']
    }
)