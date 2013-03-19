metadata = """
summary @ A collection of enhancements to the Python distutils
homepage @ http://peak.telecommunity.com/DevCenter/setuptools
license @ PSF-2
src_url @ http://cheeseshop.python.org/packages/source/s/$name/$name-0.6c11.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/python:2*
conflict @ dev-python/distribute
"""

get("python_utils")
srcdir = name + "-0.6c11"
standard_procedure = False

def install():
    python_utils_install("--prefix=/usr")
    rmfile("/usr/bin/easy_install")
