metadata = """
summary @ File manager for the Xfce desktop environment
homepage @ http://thunar.xfce.org
license @ GPL2 LGPL2.1
src_url @ http://archive.xfce.org/src/xfce/$name/1.2/Thunar-$version.tar.bz2
arch @ ~x86
"""

srcdir = "Thunar-%s" % version

#FIXME: bagimliliklari yaz

def configure():
    conf("--disable-static",
            "--enable-gio-unix",
            "--enable-dbus",
            "--enable-startup-notification",
            "--enable-gudev",
            "--enable-notifications",
            "--enable-exif",
            "--enable-pcre",
            "--disable-gtk-doc",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("update-desktop-database -q")
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
