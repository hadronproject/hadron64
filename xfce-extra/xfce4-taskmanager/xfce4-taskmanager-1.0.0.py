metadata = """
summary @ Task Manager for XFCE4
homepage @ http://goodies.xfce.org/projects/applications/xfce4-taskmanager
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/1.0/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libwnck
build @ dev-util/intltool dev-util/pkg-config
"""

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--libexecdir=/usr/lib/xfce4",
            "--localstatedir=/var",
            "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
