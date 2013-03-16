metadata = """
summary @ Power Manager for XFCE4 Desktop
homepage @ http://xfce-goodies.berlios.de/
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/1.0/$fullname.tar.bz2
arch @ ~x86_64
options @ policykit debug
"""

depends = """
runtime @ xfce-base/xfce4-panel sys-power/upower sys-fs/udisks
          x11-themes/hicolor-icon-theme gnome-base/librsvg x11-libs/libnotify
"""

opt_runtime = """
policykit @ sys-auth/polkit
"""

def configure():
    conf("--disable-network-manager",
            config_enable("policykit", "polkit"),
            "--enable-dpms",
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
