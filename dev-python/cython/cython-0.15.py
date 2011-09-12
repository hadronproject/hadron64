metadata = """
summary @ The Cython compiler for writing C extensions for the Python language
homepage @ http://www.cython.org/ http://pypi.python.org/pypi/Cython
src_url @ http://www.cython.org/release/Cython-$version.tar.gz
license @ Apache-2.0
arch @ ~x86
"""

depends = """
common @ dev-lang/python
"""

standard_procedure = False

get("python_utils")

srcdir = "Cython-%s" % version

def install():
    python_utils_install()
