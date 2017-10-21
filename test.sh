#!/bin/bash

set -e

clean(){
    rm -rf tagit.egg-info build dist *-env tagit/data
    find tagit -name '*.pyc' | xargs rm
}

setup(){
    py="$1"
    echo python${py}
    test $VIRTUAL_ENV && deactivate
    clean
    if [[ -d py${py}-env.clean ]]; then
	cp -r py${py}-env.clean py${py}-env
    else
	if [[ $py == 2 ]]; then
	    virtualenv py2-env
	else
	    python3 -m venv py3-env
	fi
	cp -r py${py}-env py${py}-env.clean
    fi
    source py${py}-env/bin/activate
}

for py in 2 3; do
    while read cmd; do
	setup $py
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



