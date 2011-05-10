metadata = """
summary @ Library to load, handle and manipulate images in the JPEG format
homepage @ http://www.ijg.org/
license @ custom
src_url @ http://www.ijg.org/files/$namesrc.v$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    copy("%s/Makefile.in.extra" % filesdir, "debian/extra/Makefile.in")
    patch(level=1)
    autoreconf("-vfi")

def configure():
    conf("--enable-shared",
            "--disable-static",
            "--enable-maxmem=64",
            "--disable-dependency-tracking")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("README")

