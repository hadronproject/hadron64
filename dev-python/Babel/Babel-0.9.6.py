metadata = """
summary @ A collection of tools for internationalizing Python applications
homepage @ http://babel.edgewall.org/
license @ BSD
src_url @ http://ftp.edgewall.com/pub/babel/$fullname.tar.gz
arch @ ~x86_64
"""

standard_procedure = False

depends = """
runtime @ dev-python/setuptools
"""

def install():
    system("python setup.py install --root=%s" % install_dir)
