metadata = """
summary @ Maps the new names of icons for Tango to the legacy names used by the GNOME and KDE desktops.
homepage @ http://tango.freedesktop.org/
license @ GPL
src_url @ http://tango.freedesktop.org/releases/$fullname.tar.bz2
arch @ ~x86
"""


depends = """
runtime @ dev-perl/XML-Simple
"""

def configure():
    raw_configure("--prefix=/usr --sysconfdir=/etc",
            "--libexecdir=/usr/lib/icon-naming-utils",
            "--localstatedir=/var")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    move("%s/usr/share/pkgconfig" % install_dir, "/usr/lib/pkgconfig")
