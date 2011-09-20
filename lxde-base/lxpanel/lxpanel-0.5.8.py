metadata = """
summary @ Panel of the LXDE Desktop
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/lxde/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ x11-libs/gtk+ dev-util/intltool
runtime @ media-libs/alsa-lib lxde-base/lxmenu-data
lxde-base/menu-cache
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
