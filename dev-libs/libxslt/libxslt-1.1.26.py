metadata = """
summary @ XML stylesheet transformation library
homepage @ http://xmlsoft.org/XSLT/
license @ MIT
src_url @ftp://xmlsoft.org/libxslt/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libxml2 dev-libs/libgcrypt
"""

def prepare():
    patch("fix-sandbox-problems.patch")
    patch("libxslt-1.1.25-fix-python-linking.patch", level=1)
    patch("libxslt.m4-libxslt-1.1.8.patch")
    autoreconf("-fi")

def configure():
    conf("--with-python")

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
