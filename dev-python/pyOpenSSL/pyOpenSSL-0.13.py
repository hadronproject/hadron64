metadata = """
summary @ Python interface to the OpenSSL library
homepage @ http://pyopenssl.sourceforge.net/
license @ Apache-2.0
src_url @ http://pypi.python.org/packages/source/p/$name/$fullname.tar.gz
arch @ ~x86_64
options @ python3
"""

depends = """
runtime @ >=dev-libs/openssl-0.9.7 dev-lang/python:2.7
"""

opt_runtime = """
python3 @ dev-lang/python:3.2
"""

standard_procedure = False

def prepare():
    system("cd .. && cp -a %s %s-python3" % (fullname, fullname))

def build():
    system("python2 setup.py build")
    if opt("python3"):
        cd("../%s-python3" % fullname)
        system("python3 setup.py build")
    

def install():
    system("python2 setup.py install --root=%s --optimize=1" % install_dir)
    if opt("python3"):
        cd("../%s-python3" % fullname)
        system("python3 setup.py install --root=%s --optimize=1" % install_dir)
