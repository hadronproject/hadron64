metadata = """
summary @ Fast lightweight tabbed filemanager
homepage @ http://pcmanfm.sourceforge.net/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
common @ sys-libs/glib x11-libs/gtk+:2 >=lxde-base/menu-cache-0.3.2
x11-libs/libfm
"""

def prepare():
    intltoolize("--force --copy --automake")
    system('sed -i -e "/MimeType/s:=.*normal;:=:" data/pcmanfm.desktop.in \ ')
    autoreconf()

def configure():
    conf(config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "ChangeLog", "COPYING", "README", 
            "NEWS")

