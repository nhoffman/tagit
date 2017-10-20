=======
 tagit
=======

Simple python package versioning with git tags

Let's say you have a Python package with the following layout::

  yourpackage/
    setup.py
    yourpackage/
      __init__.py

1. Place a copy of ``tagit/tagit.py`` in the same directory as your
   package's ``__init__.py`` (ie, in ``yourpackage/yourpackage``)

2. In your ``__init__.py`` include the following lines::

     from .tagit import get_version
     __version__ = get_version()

3. In ``setup.py``, import the variable containing the version string,
   and provide it as an argument to ``setuptools.setup()``::

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

5. Add ``version.txt`` to ``.gitignore``

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
