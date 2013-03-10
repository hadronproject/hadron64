metadata = """
summary @ A session manager for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.10/$fullname.tar.bz2
arch @ ~x86_64
options @ consolekit policykit debug
"""

depends = """
runtime @ >=xfce-base/xfce4-panel-4.10.0 x11-libs/libSM x11-libs/libwnck
          x11-themes/hicolor-icon-theme x11-apps/iceauth gnome-base/libgnome-keyring gnome-base/gconf
build @ dev-util/intltool
"""

opt_runtime = """
consolekit @ sys-auth/consolekit
policykit @ sys-auth/polkit
"""

def prepare():
    patch("xfce4-session-4.10.0-add-systemd-support.patch", level=1)

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
