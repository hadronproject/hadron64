metadata = """
summary @ Basic utility non-GUI functions for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glib dev-util/intltool
"""

def configure():
    conf(
    "--libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --disable-gtk-doc \
    --disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)
