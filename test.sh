#!/bin/bash

set -e

py2env(){
    echo python2
    test $VIRTUAL_ENV && deactivate
    rm -rf py2-env
    virtualenv py2-env
    source py2-env/bin/activate
}

py3env(){
    echo python3
    test $VIRTUAL_ENV && deactivate
    rm -rf py3-env
    python3 -m venv py3-env
    source py3-env/bin/activate
}

for setup in py2env py3env; do
    while read cmd; do
	$setup
	echo "$cmd"
	$cmd > /dev/null
	tagit --version
    done <<EOF
python setup.py install
python setup.py develop
pip install .
pip install -e .
pip install git+https://github.com/nhoffman/tagit.git
EOF
done



