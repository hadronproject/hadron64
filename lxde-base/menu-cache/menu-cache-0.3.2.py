metadata = """
summary @ Caches to speed up freedesktop.org's application menus use.
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/lxde/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-util/intltool sys-libs/glib
"""

def configure():
    raw_configure("--prefix=/usr --sysconfdir=/etc",
            "--libexecdir=/usr/lib/menu-cache --disable-static")

install = lambda: installd()
