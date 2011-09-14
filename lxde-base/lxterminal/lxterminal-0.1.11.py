metadata = """
summary @ VTE-based terminal emulator for LXDE
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/lxde/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ media-libs/fontconfig x11-libs/libX11 sys-libs/glib x11-libs/vte
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
