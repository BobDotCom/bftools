import codecs
import os.path
import re

import setuptools


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


# The full version, including alpha/beta/rc tags
with open("bftools/__init__.py") as f:
    __version__ = (
        re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
        ).group(1)
        or ""
    )

with open("README.rst") as fh:
    long_description = fh.read().replace(
        """===================
bftools
===================""",
        """===================
bftools {}
===================""".format(
            __version__
        ),
    )

extras_require = {
    "docs": [
        "sphinx==4.3.0",
        "sphinxcontrib_trio==1.1.2",
        "sphinxcontrib-websupport",
        "sphinx_rtd_theme",
    ],
    "minify": [
        "python-minifier<=2.5",
    ],
}

setuptools.setup(
    name="bftools",
    version=__version__,
    author="BobDotCom",
    author_email="bobdotcomgt@gmail.com",
    description="A brainfuck toolbox for python.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/BobDotCom/bftools",
    download_url="https://github.com/BobDotCom/bftools/releases",
    packages=setuptools.find_packages(exclude=["tests*", "build.py"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require=extras_require,
    python_requires=">=3.6",
    license="MIT",
    project_urls={
        "Documentation": "https://bftools.readthedocs.io/en/latest/index.html",
        "Source": "https://github.com/BobDotCom/bftools",
        "Tracker": "https://github.com/BobDotCom/bftools/issues",
    },
)
