metadata = """
summary @ A collection of enhancements to the Python distutils
homepage @ http://peak.telecommunity.com/DevCenter/setuptools
license @ PSF
src_url @ http://cheeseshop.python.org/packages/source/s/$name/$name-0.6c11.tar.gz
arch @ ~x86
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
    
    system("rm %s/usr/bin/easy_install" % install_dir)
    pass
