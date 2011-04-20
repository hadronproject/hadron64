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
    system("sed -i 's#-o $(PKG_USER) -g $(PKG_GROUP)##' include/buildmacros")
    autoconf()
    conf()
    system("sed -i -e 's/man2//g' man/Makefile")
    #    raw_configure("--libdir=/lib",
#                "--mandir=/usr/share/man",
#                "--libexecdir=/lib",
#                "--bindir=/bin")

def install():
    raw_install("DESTDIR=%s install install-lib install-dev" % install_dir)
