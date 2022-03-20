:github_url: https://github.com/BobDotCom/bftools

.. currentmodule:: bftools

API Reference
===============

The following section outlines the API of bftools.


.. _core_utilities:

Core Utilities
--------------
These provide the main functionality of bftools.


BrainfuckTools Class
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: BrainfuckTools
   :members:

Shortcut Functions
~~~~~~~~~~~~~~~~~~

.. autofunction:: compile

.. autofunction:: decode

.. autofunction:: encode


.. _converted_classes:

Converted Classes
-----------------
These classes are returned by various methods from the :ref:`core_utilities`.

.. autoclass:: CompiledBrainfuck
   :members:

.. autoclass:: DecodedBrainfuck
   :members:

.. autoclass:: EncodedBrainfuck
   :members:


.. _tools:

Tools
-----
These are tools that are used internally by the :ref:`core_utilities`.

.. autofunction:: factor
