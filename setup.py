from setuptools import setup, find_packages

from tagit import __version__

setup(
    author='Noah Hoffman',
    author_email='noah.hoffman@gmail.com',
    description='Simple python pachage versioning with git tags',
    url='https://github.com/nhoffman/tagit',
    name='tagit',
    packages=find_packages(),
    package_dir={'tagit': 'tagit'},
    package_data={'tagit': ['data/*']},
    version=__version__,
    entry_points={
        'console_scripts': ['tagit = tagit.main:main']
    },
    # test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
