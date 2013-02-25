metadata = """
summary @ A utility for reading man pages
homepage @ http://www.nongnu.org/man-db/
license @ GPL LGPL
src_url @ http://savannah.nongnu.org/download/man-db/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/gdbm sys-libs/libpipeline
runtime @ sys-libs/zlib sys-apps/groff
"""

def prepare():
    patch("1361_1360.diff")

def configure():
    conf("--with-db=gdbm",
        "--disable-setuid",
        "--enable-mandirs=GNU",
        '--with-sections="1 n l 8 3 0 2 5 4 9 6 7"')

def install():
    raw_install("DESTDIR=%s" % install_dir)
    rmfile("/usr/bin/zsoelim")
    # script from LFS to convert manpages, see
    # http://www.linuxfromscratch.org/lfs/view/6.4/chapter06/man-db.html
    insexe("%s/convert-mans" % filesdir, "/usr/bin/convert-mans")
    insdoc("README")
