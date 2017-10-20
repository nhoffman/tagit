import traceback
import subprocess
import os
import sys


def get_version(datadir=None, version_file='version.txt'):
    """When executed from setup.py, creates the file "{datadir}/ver"
    containing a version number corresponding to the output of 'git
    describe --tags --dirty'. In all cases, the contents of this file
    is converted into a (hopefully) PEP-440 compliant version string
    and returned. ``datadir`` is an optional path to package data;
    when not provided, assumes package data resides in a directory
    named "data" in the same directory as this file (which in turn is
    expected to be placed in the same directory as the top-level
    package __init__.py). Further notes and assumptions:

    - get_version() should be called from the package __init__.py, for example:
        from ._version import get_version
        __version__ = get_version()
    - at least one git tag is defined
    - setup.py should import
    - setuptools.setup includes a directive to include {datadir}/ver in a
      package distribution, for example
      ``setuptools.setup(package_data={'my_package': ['data/*']})``

    """

    datadir = datadir or os.path.join(os.path.dirname(__file__), 'data')
    version_file = os.path.join(datadir, version_file)

    st0 = traceback.extract_stack()[0]
    in_setup = st0.filename if hasattr(st0, 'filename') else st0[0] == 'setup.py'

    if in_setup:
        cmd = ['git', 'describe', '--tags', '--dirty']

        try:
            os.makedirs(datadir)
        except OSError:
            pass

        try:
            git_version = subprocess.check_output(cmd, universal_newlines=True)
        except Exception:
            sys.stderr.write('error running "{}"\n'.format(' '.join(cmd)))
        else:
            version = git_version.strip().replace('-', '+', 1).replace('-', '.')
            with open(version_file, 'w') as f:
                f.write(version)

    try:
        with open(version_file) as f:
            version = f.read()
    except Exception:
        version = ''

    return version
