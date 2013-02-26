metadata = """
summary @ POSIX 1003.1e capabilities
homepage @ http://www.kernel.org/pub/linux/libs/security/linux-privs/
license @ GPL
src_url @ ftp://ftp.archlinux.org/other/libcap/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-apps/attr
"""

def install():
    raw_install("prefix=/usr DESTDIR=%s RAISE_SETFCAP=no" % install_dir)
    setmod("755 %s/usr/lib64/libcap.so.%s" % (install_dir, raw_version))
    rmfile("/usr/lib64/libcap.a")
