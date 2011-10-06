metadata = """
summary @ Linux terminal based on classic terminals from first person shooter games
homepage @ http://tilda.sourceforge.net/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/tilda/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/confuse x11-libs/vte gnome-base/libglade sys-libs/glib
build @ sys-apps/gawk dev-util/pkg-config
"""

def prepare():
    patch("gdk_resources.patch", level=1)
    patch("tilda-0.9.6-palette.patch")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "README", "TODO")
