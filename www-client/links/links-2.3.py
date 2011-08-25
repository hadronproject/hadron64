metadata = """
summary @ A text WWW browser, similar to Lynx
homepage @ http://links.twibright.com/
license @ GPL
src_url @ http://links.twibright.com/download/$name-2.3pre2.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ app-arch/bzip2 sys-libs/zlib dev-libs/openssl sys-libs/gpm
build @ media-libs/tiff media-libs/libpng x11-libs/libXt
"""

srcdir = "links-2.3pre2"

def configure():
    conf("--enable-javascript",
            "--disable-graphics",
            "--without-x",
            "--without-fb")

def install():
    raw_install("DESTDIR=%s" % install_dir)
