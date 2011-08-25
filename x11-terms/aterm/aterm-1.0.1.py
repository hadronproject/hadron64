metadata = """
summary @ An xterm replacement with transparency support
homepage @ http://aterm.sourceforge.net/
license @ GPL
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-libs/libSM
"""

def configure():
    conf(
    "--enable-transparency=yes \
    --enable-background-image --enable-fading --enable-menubar \
    --enable-graphics")

def install():
    raw_install("DESTDIR=%s" % install_dir)
