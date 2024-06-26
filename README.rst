HydrOffice ABC 2
================

.. image:: https://github.com/hydroffice/hyo2_abc2/raw/master/hyo2/abc2/app/pkg_info/media/app_icon.png
    :alt: logo

|

.. image:: https://img.shields.io/pypi/v/hyo2.abc2.svg
    :target: https://pypi.python.org/pypi/hyo2.abc2
    :alt: PyPi version

.. image:: https://github.com/hydroffice/hyo2_abc2/actions/workflows/abc2_on_windows.yml/badge.svg
    :target: https://github.com/hydroffice/hyo2_abc2/actions/workflows/abc2_on_windows.yml
    :alt: Windows

.. image:: https://github.com/hydroffice/hyo2_abc2/actions/workflows/abc2_on_linux.yml/badge.svg
    :target: https://github.com/hydroffice/hyo2_abc2/actions/workflows/abc2_on_linux.yml
    :alt: Linux

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
    :target: https://www.hydroffice.org/manuals/abc2/index.html
    :alt: Latest Documentation

.. image:: https://app.codacy.com/project/badge/Grade/6f90f01fa2ce4eef9ceaec9b4b2ba591
    :target: https://app.codacy.com/gh/hydroffice/hyo2_abc2/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
    :alt: codacy

.. image:: https://coveralls.io/repos/github/hydroffice/hyo2_abc2/badge.svg?branch=master
    :target: https://coveralls.io/github/hydroffice/hyo2_abc2?branch=master
    :alt: coverall

|

* GitHub: `https://github.com/hydroffice/hyo2_abc2 <https://github.com/hydroffice/hyo2_abc2>`_
* Project page: `url <https://www.hydroffice.org>`_
* License: LGPLv3

|

General info
------------

HydrOffice is a research development environment for ocean mapping. It provides a collection of hydro-packages,
each of them dealing with a specific issue of the field.
The main goal is to speed up both algorithms testing and research-2-operation.

The ABC package provides common elements for HydrOffice libraries and applications.

Main library features:

* A PkgInfo class (to collect info about the library and the app)
* Helper class
* A GDAL Aux class (to help with GDAL handling)
* CLI Progress Bar class

Main GUI features:

* An AppStyle class (to manage app styles)
* A Browser widget
* An S57 NOAA Support Files app
* A Package Info app (with Exception dialog, About dialog and Qt-based Progress Bar class)
* A report tool

|

Credits
-------

Authors
~~~~~~~

This code is written and maintained by:

- `Giuseppe Masetti <mailto:gmasetti@ccom.unh.edu>`_


Contributors
~~~~~~~~~~~~

The following wonderful people contributed directly or indirectly to this project:

- `Lachlan Hurst <mailto:lhurst@frontiersi.com.au>`_

Please add yourself here alphabetically when you submit your first pull request.

|

Testing
~~~~~~~

For running tests and check the relative coverage:

.. code-block::

    coverage run --source hyo2 setup.py test

To get the test coverage report:

.. code-block::

    coverage report -m

and/or:

.. code-block::

    coverage html
    open html_cov/index.html
