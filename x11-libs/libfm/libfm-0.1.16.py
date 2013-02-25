metadata = """
summary @ the core of next generation file manager PCManFM
homepage @ http://pcmanfm.sourceforge.net/
license @ GPL-3
src_url @ http://downloads.sourceforge.net/pcmanfm/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-libs/dbus-glib >=lxde-base/menu-cache-0.3.2 x11-libs/gtk+:2 sys-libs/glib
runtime @ x11-misc/shared-mime-info sys-fs/udisks
"""

def prepare():
    system("sed -i '/docs/d' configure.ac")
    autoreconf()
    system("sed -i 's/GTK_DOC_CHECK(1.14,--flavour no-tmpl)/#GTK_DOC_CHECK(1.14,--flavour no-tmpl)/' configure")

def configure():
	conf("--prefix=/usr --sysconfdir=/etc --enable-udisks --with-gnu-ld",
            "--disable-dependency-tracking --disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

def post_install():
	system("update-mime-database /usr/share/mime > /dev/null")
	system("update-desktop-database -q")
	system("gio-querymodules /usr/lib/gio/modules")
