metadata = """
summary @ A library which provides a secure layer over a reliable transport layer
homepage @ http://www.gnu.org/software/gnutls/
license @ GPL3 + LGPL
src_url @ ftp://ftp.gnu.org/gnu/gnutls/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libtasn1 sys-apps/readline sys-libs/zlib dev-libs/libgcrypt sys-devel/gcc
"""

def configure():
    conf(
    "--prefix=/usr \
    --with-zlib \
    --with-libgcrypt \
    --disable-static \
    --disable-guile")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    makesym("/usr/lib/libgnutls.so", "/usr/lib/libgnutls.so.28")
