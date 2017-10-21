import traceback
import subprocess
import os
import sys


def get_version(datadir=None, version_file='version.txt'):
    """When executed from setup.py, creates the file "{datadir}/ver"
    containing a version number corresponding to the output of 'git
    describe --tags --dirty'. In all cases, the contents of this file
    is converted into a (hopefully) PEP-440 compliant version string
    and returned.

    """

    datadir = datadir or os.path.join(os.path.dirname(__file__), 'data')
    version_file = os.path.join(datadir, version_file)

    # only try to create the version file if setup.py is someplace in the stack
    stack = traceback.extract_stack()

    stackstr = str(stack)
    with open('/Users/nhoffman/src/tagit/stack-{}.txt'.format(hash(stackstr)), 'w') as f:
        f.write(stackstr)

    try:
        in_setup = any(s.filename.endswith('setup.py') for s in stack)
    except AttributeError:
        in_setup = any(s[0].endswith('setup.py') for s in stack)

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
