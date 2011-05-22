metadata = """
summary @ A session manager for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/xfce4-panel x11-libs/libSM x11-libs/libwnck sys-power/upower sys-auth/consolekit
          x11-themes/hicolor-icon-theme x11-apps/iceauth gnome-base/libgnome-keyring gnome-base/gconf
build @ dev-util/intltool
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
            "--enable-upower",
            "--enable-consolekit",
            "--enable-polkit",
            "--enable-panel-plugin",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    makedirs("/etc/polkit-1/localauthority")
    makedirs("/etc/polkit-1/localauthority/50-local.d")

    insfile("%s/org.freedesktop.consolekit.pkla" % filesdir, 
            "/etc/polkit-1/localauthority/50-local.d/org.freedesktop.consolekit.pkla")

    insfile("%s/org.freedesktop.upower.pkla" % filesdir, 
            "/etc/polkit-1/localauthority/50-local.d/org.freedesktop.upower.pkla")
