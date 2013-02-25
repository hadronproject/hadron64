metadata = """
summary @ Bazaar is a next generation distributed version control system.
homepage @ http://bazaar-vcs.org/
license @ GPL-2
src_url @ http://launchpad.net/bzr/2.4/$version/+download/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-lang/python dev-python/cython
"""

standard_procedure=False

get("python_utils")

def prepare():
    patch("bzr-2.4.0-no-pyrex-citon.patch")

def build():
    sed("-i 's|man/man1|share/man/man1|' setup.py")
    python_utils_build()

def install():
    python_utils_install()
