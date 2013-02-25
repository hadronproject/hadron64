metadata = """
summary @ A panel plugin that uses indicator-applet to show new messages
homepage @ http://goodies.xfce.org/projects/panel-plugins/xfce4-indicator-plugin
license @ GPL-2 LGPL-2
src_url @ http://archive.xfce.org/src/panel-plugins/$name/0.3/$fullname.tar.bz2
options @ debug
arch @ ~x86_64
"""

depends = """
runtime @ >=dev-libs/libindicator-0.3.0 x11-libs/gtk+:2 
>=xfce-base/libxfce4util-4.3.99.2
>=xfce-base/xfce4-panel-4.3.99.2
"""

def configure():
    conf("--disable-static",
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
