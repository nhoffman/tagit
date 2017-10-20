=======
 tagit
=======

Simple python package versioning with git tags

why?
====

There are tons of projects like this (most famously, versioneer). But
I have converged on this tiny and lightweight solution over the years,
and it meets my (minimal) requirements. Just commit a single small
file to your project, sprinkle in a few imports, and that's it.

The idea is that version numbers are defined entirely by git tags with
no additional effort. Version numbers correspond to the output of
``git describe --tags --dirty``, with some minimal modification to be
more likely to comply with PEP-440 (one assumption here is that
PEP-440 is mainly intended to govern version numbers of software
releases, and we aren't going to work too hard to comply in other
contexts). Use of this package assumes that tags will follow the
convention ``major[.minor[.point]]``, eg::

  git tag -a -m "version 0.9.1" 0.9.1

configuration
=============

Let's say you have a Python package with the following repository layout::

  yourpackage/
    setup.py
    yourpackage/
      __init__.py

1. Add and commit a copy of ``tagit/tagit.py`` in the same directory as your
   package's ``__init__.py`` (ie, in ``yourpackage/yourpackage``)::

     cd yourpackage
     curl ...

2. In your ``__init__.py`` include the following lines::

     from yourpackage.tagit import get_version
     __version__ = get_version()

3. In ``setup.py``, import the variable containing the version string
   (``yourpackage.__version__``), and provide it as an argument to
   ``setuptools.setup()``. You must also make sure that the contents
   of ``yourpackage/data`` is included in distributions of your
   package (ie, the output of ``setup.py sdist``)::

     from setuptools import setup

     from yourpackage import __version__

     setup(
         ...,
	 version=__version__,
	 package_data={'yourpackage': ['data/*']}
	 )

4. If your package includes a command line interface using
   ``argparse``, define an option to print the version::

     import argparse
     from yourpackage import __version__

     parser = argparse.ArgumentParser(description=__doc__)
     parser.add_argument('-V', '--version', action='version',
                         version='%(prog)s {}'.format(__version__))
     args = parser.parse_args(arguments or sys.argv[1:])

5. Add ``version.txt`` to ``.gitignore`` - this is the file containing
   the version string, and is either generated when ``setup.py`` is
   run, or included with the package distribution. It should never be
   committed to your repository.

6. Initial creation of a package data directory and a text file
   containing the version string occurs when you first run
   ``setup.py``, for example ``python setup.py clean`` will do it.

That should be it! After the above steps, your package should now
minimally contain::

  yourpackage/
    .gitignore
    setup.py
    yourpackage/
      data/version.txt
      __init__.py
      tagit.py

This repo provides an example of a minimal package with the necessary
elements::

  tagit % tree
  .
  |-- README.rst
  |-- setup.py
  |-- tagit
  |   |-- __init__.py
  |   |-- data
  |   |   `-- version.txt
  |   |-- main.py
  |   `-- tagit.py
  `-- tagit.py
