metadata = """
summary @ GTK+ theme switcher of the LXDE Desktop (manages icons and fonts)
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/lxde/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-util/intltool
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
