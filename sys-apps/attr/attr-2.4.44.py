metadata = """
summary @ Extended attribute support library for ACL support
homepage @ http://oss.sgi.com/projects/xfs/
license @ LGPL-2
src_url @ http://download.savannah.gnu.org/releases-noredirect/$name/$fullname.src.tar.gz
arch @ ~x86
"""

def prepare():
    patch(level=1)

def configure():
    raw_configure("--libdir=/lib",
                "--mandir=/usr/share/man",
                "--libexecdir=/lib",
                "--bindir=/bin")

def install():
    raw_install("DESTDIR=%s install install-lib install-dev" % install_dir)
