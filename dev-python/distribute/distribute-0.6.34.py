metadata = """
summary @ Distribute (fork of Setuptools) is a collection of extensions to Distutils
homepage @ http://pypi.python.org/pypi/distribute
license @ PSF-2
src_url @ http://pypi.python.org/packages/source/d/distribute/distribute-$version.tar.gz
arch @ ~x86_64
"""

# FIXME python3 support

depends = """
common @ dev-lang/python:2*
conflict @ dev-python/setuptools
"""
get("main/python_utils")

standard_procedure = False

def build():
    python_utils_build()

def install():
    python_utils_install()
