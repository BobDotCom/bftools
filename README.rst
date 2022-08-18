===================
bftools
===================

A brainfuck toolbox for python.

|Status badge| |Docs badge| |Downloads badge|

.. |Status badge| image:: https://github.com/BobDotCom/bftools/workflows/Python%20Package/badge.svg
   :target: https://github.com/BobDotCom/bftools/actions?query=workflow%3A"Python+Package"
   :alt: Package Status

.. |Docs badge| image:: https://readthedocs.org/projects/bftools/badge/?version=latest
   :target: https://bftools.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |Downloads badge| image:: https://static.pepy.tech/personalized-badge/bftools?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
   :target: https://pepy.tech/project/bftools
   :alt: Download Counter

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
