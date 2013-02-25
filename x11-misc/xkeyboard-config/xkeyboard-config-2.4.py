metadata = """
summary @ X keyboard configuration files
homepage @ http://www.freedesktop.org/wiki/Software/XKeyboardConfig
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/data/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-apps/xkbcomp
build @ dev-util/intltool dev-perl/XML-Parser
"""

def configure():
    conf("--with-xkb-base=/usr/share/X11/xkb \
            --with-xkb-rules-symlink=xorg \
            --enable-compat-rules=yes")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
