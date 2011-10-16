metadata = """
summary @ A notepad clone for GTK+ 2.0
homepage @ http://tarot.freeshell.org/leafpad/
license @ GPL
src_url @ http://download.savannah.gnu.org/releases/$name/$name-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ >=x11-libs/gtk+-2.10:2
build @ sys-devel/gettext dev-util/intltool dev-util/pkg-config
"""

def configure():
    conf(
    "--disable-dependency-tracking",
    "--enable-chooser",
    "--enable-print")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
    system("echo 'StartupNotify=true' >> %s/usr/share/applications/leafpad.desktop" % install_dir)

def post_install():
    system("update-desktop-database -q")
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

def post_remove():
    post_install()
