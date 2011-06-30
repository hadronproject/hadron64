metadata = """
summary @ Plugin to switch keyboard layouts for the XFCE4 panel
homepage @ http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
license @ custom
src_url @ http://archive.xfce.org/src/panel-plugins/$name/0.5/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/xfce4-panel x11-libs/libXklavier gnome-base/librsvg
build @ dev-util/intltool
"""

def configure():
    conf("--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
