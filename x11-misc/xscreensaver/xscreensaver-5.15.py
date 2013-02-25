metadata = """
summary @ Screen saver and locker for the X Window System
homepage @ http://www.jwz.org/xscreensaver/
license @ BSD
src_url @ http://www.jwz.org/xscreensaver/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXmu x11-libs/libXxf86vm x11-libs/libXrandr x11-libs/libXxf86misc
x11-libs/libXt x11-libs/libXext x11-libs/libXi x11-apps/appres media-libs/mesa sys-libs/pam
>=dev-libs/libxml2-2.5 >=x11-libs/gtk+-2:2 >=gnome-base/libglade-1.9
build @ sys-devel/bc
"""

def configure():
    conf("--with-x-app-defaults=/usr/share/X11/app-defaults",
            "--with-pam", "--without-motif", "--with-gtk", "--with-gl",
            "--without-gle", "--with-xpm", "--with-pixbuf", "--with-jpeg")

def install():
    raw_install("install_prefix=%s" % install_dir)
    insfile("%s/LICENSE" % filesdir, "/usr/share/licenses/xscreensaver/LICENSE")
    insfile("%s/xscreensaver.pam" % filesdir, "/etc/pam.d/xscreensaver")
    setmod("755", "%s/usr/bin/xscreensaver" % install_dir)
    echo("NotShowIn=KDE;GNOME;", "/usr/share/applications/xscreensaver-properties.desktop")
