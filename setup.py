from setuptools import setup
import binarytree_test

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name=binarytree_test.__appname__,
    version=binarytree_test.__version__,
    author=binarytree_test.__author__,
    author_email=binarytree_test.__email__,
    description=binarytree_test.__description__,
    license=binarytree_test.__license__,
    long_description=__doc__,
    install_requires=required,
    packages=[binarytree_test.__appname__],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache2',
        'Topic :: Utilities'
    ],
    entry_points={
        "console_scripts": ['binarytree_api = binarytree_test.main:main']
    },
    zip_safe=False

    #scripts=['binarytree_test.py'],
)
