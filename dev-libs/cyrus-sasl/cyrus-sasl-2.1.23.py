metadata = """
summary @ Cyrus Simple Authentication Service Layer (SASL) library
homepage @ http://cyrusimap.web.cmu.edu/downloads.html#sasl
license @ as-is
src_url @ ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/db sys-libs/pam
"""

def prepare():
    patch("cyrus-sasl-2.1.19-checkpw.c.patch", level=0)
    patch("cyrus-sasl-db.patch", level=1)

def configure():
    conf("--disable-anon \
            --disable-cram \
            --disable-digest \
            --disable-gssapi \
            --enable-login \
            --disable-otp \
            --enable-plain")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
