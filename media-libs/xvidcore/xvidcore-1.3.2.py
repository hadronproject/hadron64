metadata = """
summary @ XviD is an open source MPEG-4 video codec
homepage @ http://www.xvid.org/
license @ GPL
src_url @ http://downloads.xvid.org/downloads/$name-$version.tar.bz2
arch @ ~x86_64
options @ threads pic
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/yasm
"""

srcdir = "xvidcore"

def configure():
    myconf = ""
    if opt("pic"):
        myconf += " --disable-assembly "

    cd("build/generic")
    conf(
    config_enable("threads", "pthread"), myconf)

def build():
    cd("build/generic")
    make()

def install():
    cd("build/generic")
    raw_install("DESTDIR=%s" % install_dir)

#       insdoc("COPYING")
