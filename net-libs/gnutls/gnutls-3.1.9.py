metadata = """
summary @ A library which provides a secure layer over a reliable transport layer
homepage @ http://www.gnu.org/software/gnutls/
license @ GPL3 + LGPL
src_url @ ftp://ftp.gnutls.org/gcrypt/gnutls/v3.1/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ app-arch/xz
runtime @ sys-libs/glibc dev-libs/libtasn1 sys-libs/readline 
sys-libs/zlib dev-libs/libgcrypt sys-devel/gcc dev-libs/nettle[gmp]
"""

def configure():
    conf(
    "--prefix=/usr",
    "--with-zlib",
    "--disable-static",
    "--disable-guile",
    "--disable-valgrind-tests")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    makesym("/usr/lib/libgnutls.so", "/usr/lib/libgnutls.so.28")
