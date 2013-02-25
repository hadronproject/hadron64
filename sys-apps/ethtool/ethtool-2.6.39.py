metadata = """
summary @ gkernel ethtool
homepage @ http://www.kernel.org/pub/software/network/ethtool/
license @ GPL
src_url @ http://ftp.eu.openbsd.org/pub/mirrors/ftp.kernel.org/software/network/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    "--prefix=/usr --mandir=/usr/share/man")

def install():
    raw_install("DESTDIR=%s" % install_dir)
