metadata = """
summary @ Support library for libgcrypt
homepage @ http://www.gnupg.org/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/libgpg-error/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

