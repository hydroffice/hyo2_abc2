HydrOffice ABC
==============

.. image:: https://github.com/hydroffice/hyo2_abc2/raw/master/hyo2/abc2/app/media/app_icon.png
    :alt: logo

|

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
    :target: https://www.hydroffice.org/manuals/abc2/index.html
    :alt: Latest Documentation

.. image:: https://travis-ci.com/hydroffice/hyo2_abc2.svg?branch=master
    :target: https://travis-ci.com/hydroffice/hyo2_abc2
    :alt: travis-ci

.. image:: https://ci.appveyor.com/api/projects/status/5n34b7egbwmld84j?svg=true
    :target: https://ci.appveyor.com/project/giumas/hyo2-abc2
    :alt: appveyor

.. image:: https://app.codacy.com/project/badge/Grade/6f90f01fa2ce4eef9ceaec9b4b2ba591
    :target: https://www.codacy.com/gh/hydroffice/hyo2_abc2/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hydroffice/hyo2_abc2&amp;utm_campaign=Badge_Grade
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

* A LibInfo class (to collect info about the library)
* Helper class
* A GDAL Aux class (to help with GDAL handling)
* CLI Progress Bar class

Main GUI features:

* An AppInfo class (to collect info about the app)
* An AppStyle class (to manage app styles)
* A Browser widget
* An Info tab
* An Exception dialog
* An About dialog
* A Qt-based Progress Bar class

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
