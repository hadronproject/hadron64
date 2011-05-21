metadata = """
summary @ a simple client-server configuration storage and query system
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/libxfce4util sys-apps/dbus x11-libs/gtk+
"""

def configure():
    conf("--libexecdir=/usr/lib/xfce4",
            "--disable-static",
            "--disable-gtk-doc",
            '--with-perl-options=INSTALLDIRS="vendor"',
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

