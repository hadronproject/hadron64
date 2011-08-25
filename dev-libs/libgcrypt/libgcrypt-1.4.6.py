metadata = """
summary @ a general purpose crypto library based on the code used
homepage @ http://www.gnupg.org/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/libgcrypt/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc >dev-libs/libgpg-error-1.9
"""

def configure():
    conf(
    "--prefix=/usr",
    "--disable-static",
    "--disable-padlock-support")

def install():
    raw_install("DESTDIR=%s" % install_dir)
