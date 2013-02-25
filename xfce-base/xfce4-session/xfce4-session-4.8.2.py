metadata = """
summary @ A session manager for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86_64
options @ consolekit policykit debug udev
"""

depends = """
runtime @ xfce-base/xfce4-panel x11-libs/libSM x11-libs/libwnck
          x11-themes/hicolor-icon-theme x11-apps/iceauth gnome-base/libgnome-keyring gnome-base/gconf
build @ dev-util/intltool
"""

opt_runtime = """
consolekit @ sys-auth/consolekit
policykit @ sys-auth/polkit
udev @ sys-power/upower
"""

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--libexecdir=/usr/lib/xfce4",
            "--localstatedir=/var",
            "--disable-static",
            "--disable-hal",
            "--enable-gnome",
            "--enable-libgnome-keyring",
            "--enable-session-screenshots",
            config_enable("udev", "upower"),
            config_enable("consolekit"),
            config_enable("policykit", "polkit"),
            "--enable-panel-plugin",
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makedirs("/etc/polkit-1/localauthority")
    makedirs("/etc/polkit-1/localauthority/50-local.d")

    insfile("%s/org.freedesktop.consolekit.pkla" % filesdir,
            "/etc/polkit-1/localauthority/50-local.d/org.freedesktop.consolekit.pkla")

    insfile("%s/org.freedesktop.upower.pkla" % filesdir,
            "/etc/polkit-1/localauthority/50-local.d/org.freedesktop.upower.pkla")
