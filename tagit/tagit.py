"""
MIT License

Copyright (c) 2017 Noah Hoffman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import traceback
import subprocess
import os
import sys


def get_version(datadir=None, version_file='version.txt'):
    """When executed from setup.py, creates the file "{datadir}/{version_file}"
    containing a version number corresponding to the output of 'git
    describe --tags --dirty'. In all cases, the contents of this file
    is converted into a (hopefully) PEP-440 compliant version string
    and returned.

    For complete instructions, see https://github.com/nhoffman/tagit
    """

    datadir = datadir or os.path.join(os.path.dirname(__file__), 'data')
    version_file = os.path.join(datadir, version_file)

    # only try to create the version file if setup.py is someplace in the stack
    stack = traceback.extract_stack()

    try:
        in_setup = any(s.filename.endswith('setup.py') for s in stack)
    except AttributeError:
        in_setup = any(s[0].endswith('setup.py') for s in stack)

    with open('/Users/nhoffman/src/tagit/log-{}.txt'.hash(str(stack))) as f:
        for e in stack:
            f.write(str(e) + '\n')

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
