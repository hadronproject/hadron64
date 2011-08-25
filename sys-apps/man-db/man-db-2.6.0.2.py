metadata = """
summary @ A utility for reading man pages
homepage @ http://www.nongnu.org/man-db/
license @ GPL LGPL
src_url @ http://savannah.nongnu.org/download/man-db/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/gdbm sys-libs/zlib sys-libs/libpipeline sys-apps/groff

build @ sys-libs/gdbm sys-libs/libpipeline
"""

def configure():
    conf("--with-db=gdbm",
        "--disable-setuid",
        "--enable-mandirs=GNU",
        '--with-sections="1 n l 8 3 0 2 5 4 9 6 7"')

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("README")
