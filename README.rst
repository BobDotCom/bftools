===================
bftools
===================

|Mypy| |Pylint| |Black|

|Codecov| |Checks| |Lint| |Tests|

|PyPI| |Versions| |Docs badge| |Downloads badge| |GitHub|

A brainfuck toolbox for python.

.. |Mypy| image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
   :alt: Checked with mypy
.. |Pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
   :target: https://github.com/PyCQA/pylint
   :alt: linting: pylint
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

.. |Codecov| image:: https://codecov.io/gh/BobDotCom/bftools/branch/main/graph/badge.svg?token=3FTK3MPDBI
   :target: https://codecov.io/gh/BobDotCom/bftools
   :alt: Codecov
.. |Checks| image:: https://github.com/BobDotCom/bftools/actions/workflows/check.yml/badge.svg
   :target: https://github.com/BobDotCom/bftools/actions/workflows/check.yml
   :alt: Checks
.. |Lint| image:: https://github.com/BobDotCom/bftools/actions/workflows/lint.yml/badge.svg
   :target: https://github.com/BobDotCom/bftools/actions/workflows/lint.yml
   :alt: Type Check and Lint
.. |Tests| image:: https://github.com/BobDotCom/bftools/actions/workflows/test.yml/badge.svg
   :target: https://github.com/BobDotCom/bftools/actions/workflows/test.yml
   :alt: Unit Tests

.. |PyPI| image:: https://img.shields.io/pypi/v/bftools.svg?logo=pypi&color=yellowgreen&logoColor=white
   :target: https://pypi.python.org/pypi/py-cord
   :alt: PyPI version info
.. |Versions| image:: https://img.shields.io/pypi/pyversions/bftools.svg?logo=python&logoColor=white
   :target: https://pypi.python.org/pypi/py-cord
   :alt: PyPI supported Python versions
.. |Docs badge| image:: https://readthedocs.org/projects/bftools/badge/?version=latest
   :target: https://bftools.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. |Downloads badge| image:: https://static.pepy.tech/personalized-badge/bftools?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
   :target: https://pepy.tech/project/bftools
   :alt: Download Counter
.. |GitHub| image:: https://img.shields.io/github/v/release/BobDotCom/bftools?include_prereleases&label=Latest%20Release&logo=github&sort=semver&logoColor=white
   :target: https://github.com/BobDotCom/bftools/releases
   :alt: Latest release

PyPI: https://pypi.org/project/bftools/

Docs: https://bftools.readthedocs.io/en/latest/

Installation
############
You can install released versions of bftools from the Python Package Index via pip or a similar tool:

**Stable Release:** ``pip install bftools``

**Working Version:** ``pip install git+https://github.com/BobDotCom/bftools.git``

Usage
#####

.. code-block:: python

    import bftools
    comp = bftools.BrainfuckTools()
    py = comp.compile("++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++++++.---------------.++++++++++++++.+.")
    print(py.code)
