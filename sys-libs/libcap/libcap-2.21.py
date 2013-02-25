metadata = """
summary @ POSIX 1003.1e capabilities
homepage @ http://www.kernel.org/pub/linux/libs/security/linux-privs/
license @ GPL
src_url @ http://ftp.eu.openbsd.org/pub/mirrors/ftp.kernel.org/linux/libs/security/linux-privs/libcap2/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-apps/attr
"""

def prepare():
    patch("libcap-2.20-ignore-RAISE_SETFCAP-install-failures.patch", level=1)
    patch("libcap-2.20-build-system-fixes.patch", level=1)
    patch("libcap-2.21-include.patch")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    #raw_install("prefix=/usr DESTDIR=%s LIBDIR=%s/lib RAISE_SETFCAP=no" % ((install_dir),2))
