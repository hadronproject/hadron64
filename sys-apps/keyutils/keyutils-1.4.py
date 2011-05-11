metadata = """
summary @ Linux Key Management Utilities
homepage @ http://www.kernel.org/
license @ GPL2 + LGPL2.1
src_url @ http://people.redhat.com/~dhowells/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

