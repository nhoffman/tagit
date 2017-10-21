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

    logfile = open(
        '/Users/nhoffman/src/tagit/stack-{}.txt'.format(hash(str(stack))), 'w')
    for e in stack:
        logfile.write(str(e) + '\n')
    logfile.close()

    try:
        in_setup = any(s.filename.endswith('setup.py') for s in stack)
    except AttributeError:
        in_setup = any(s[0].endswith('setup.py') for s in stack)

    if in_setup:
        sys.stdout.write('updating {} with version '.format(version_file))
        subprocess.call(
            ('mkdir -p {datadir} && '
             'git describe --tags --dirty > {file}.tmp '
             '&& mv {file}.tmp {file} '
             '|| rm -f {file}.tmp').format(datadir=datadir, file=version_file),
            shell=True, stderr=open(os.devnull, "w"))

    try:
        with open(version_file) as f:
            version = f.read().strip().replace('-', '+', 1).replace('-', '.')
    except Exception:
        version = ''

    return version
