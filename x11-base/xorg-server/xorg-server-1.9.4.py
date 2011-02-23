metadata = """
summary @ X.Org X servers
homepage @ http://www.x.org
license @ GPL-2
src_url @ http://xorg.freedesktop.org//releases/individual/xserver/$name-$version.tar.bz2
options @ ipv6 nptl udev xorg dmx doc kdrive minimal static-libs tslib
"""

def configure():
    autoreconf("-fiv")
    conf(config_enable("ipv6"),
        config_enable("dmx"),
        config_enable("kdrive"),
        config_enable("udev", "config_udev"),
        config_enable("xorg"),
        config_enable("static-libs", "static"),
        "--disable-config-hal",
        "--disable-config-dbus",
        "--enable-xephyr",
        "--enable-glx-tls",
        "--enable-install-setuid",
        "--enable-record",
        "--disable-xfake",
        "--disable-xfbdev",
        "--enable-dri",
        "--enable-xvfb",
        "--enable-xnest",
        "--enable-composite",
        "--with-os-name=\'Hadron\'",
        "--with-os-vendor=\'Hadron Project\'",
        "--with-fontrootdir=/usr/share/fonts",
        "--with-xkb-path=/usr/share/X11/xkb",
        "--sysconfdir=/etc/X11",
        "--localstatedir=/var",
        "--with-xkb-output=/var/lib/xcb",
        "--with-dri-driver-path=/usr/lib/xorg/modules/dri")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    for dirname in ("etc/X11/fontpath.d", "/etc/X11/xorg.conf.d", 
            "/usr/share/X11/pci", "/usr/share/X11/xorg.conf.d"):
        makedirs(dirname)
