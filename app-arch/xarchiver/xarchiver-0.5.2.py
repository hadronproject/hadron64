metadata = """
summary @ GTK+ frontend to various command line archivers
homepage @ http://xarchiver.sourceforge.net
license @ GPL
src_url @ http://downloads.sourceforge.net/xarchiver/xarchiver-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-util/desktop-file-utils x11-themes/hicolor-icon-theme
build @ dev-util/intltool
"""

def configure():
    raw_configure("--prefix=/usr",
            "--libexecdir=/usr/lib/xfce4")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("update-desktop-database -q")
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
