metadata = """
summary @ POSIX 1003.1e capabilities
homepage @ http://www.kernel.org/pub/linux/libs/security/linux-privs/
license @ GPL
src_url @ http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-apps/attr
"""

def install():
    raw_install("prefix=/usr DESTDIR=%s LIBDIR=%s/lib RAISE_SETFCAP=no" % ((install_dir),2))
