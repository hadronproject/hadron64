metadata = """
summary @ XML parsing library, version 2
homepage @ http://www.xmlsoft.org/
license @ custom
src_url @ ftp://ftp.xmlsoft.org/libxml2/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-apps/readline sys-libs/ncurses sys-libs/zlib
"""

def prepare():
    patch(level=1)

def configure():
    autoreconf("-fi")
    conf("--with-threads --with-history \
            --with-python=/usr/bin/python2.7")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
