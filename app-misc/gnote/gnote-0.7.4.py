metadata = """
summary @ Desktop note-taking application
homepage @ http://live.gnome.org/Gnote
license @ GPL3
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.7/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-cpp/gtkmm dev-libs/libxslt
build @ dev-util/intltool app-text/gnome-doc-utils dev-libs/boost
"""

def configure():
    conf("--disable-scrollkeeper",
            "--disable-schemas-install",
            "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makedirs("/usr/share/gconf/schemas")


def post_install():
    system('gconf-merge-schema "/usr/share/gconf/schemas/gnote.schemas" \
            --domain gnote /etc/gconf/schemas/*.schemas')

    system("/usr/sbin/gconfpkg --install gnote")
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
