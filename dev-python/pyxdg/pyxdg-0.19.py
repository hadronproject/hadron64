metadata = """
summary @ Python library to access freedesktop.org standards.
homepage @ http://freedesktop.org/Software/pyxdg
license @ "LGPL"
src_url @ http://www.freedesktop.org/~lanius/$name-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/python:2.7
"""

standard_procedure = False

def install():
    system("python2 setup.py install --prefix=/usr --root=%s" % install_dir)
