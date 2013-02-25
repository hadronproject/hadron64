metadata = """
summary @ Date and time display plugin for the Xfce panel
homepage @ http://xfce-goodies.berlios.de
license @ GPL2
src_url @ http://archive.xfce.org/src/panel-plugins/$name/0.6/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ xfce-base/xfce4-panel
build @ dev-util/intltool
"""

def configure():
    conf("--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
