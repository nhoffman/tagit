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

    logfile = open('/Users/nhoffman/src/tagit/stack-{}.txt'.format(hash(str(stack))), 'w')
    for e in stack:
        logfile.write(str(e) + '\n')

    try:
        in_setup = any(s.filename.endswith('setup.py') for s in stack)
    except AttributeError:
        in_setup = any(s[0].endswith('setup.py') for s in stack)

    logfile.write('in_setup: {}\n'.format(in_setup))

    if in_setup:
        cmd = ['git', 'describe', '--tags', '--dirty']

        try:
            os.makedirs(datadir)
        except OSError:
            pass

        try:
            git_version = subprocess.check_output(cmd, universal_newlines=True)
        except Exception as err:
            sys.stderr.write('error running "{}"\n'.format(' '.join(cmd)))
            logfile.write(str(err) + '\n')
        else:
            version = git_version.strip().replace('-', '+', 1).replace('-', '.')
            with open(version_file, 'w') as f:
                f.write(version)

    try:
        with open(version_file) as f:
            version = f.read()
    except Exception as err:
        logfile.write(str(err) + '\n')
        version = ''

    return version
