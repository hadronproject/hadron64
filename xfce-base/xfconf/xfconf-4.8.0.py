metadata = """
summary @ a simple client-server configuration storage and query system
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86_64
options @ debug
"""

depends = """
runtime @ xfce-base/libxfce4util dev-libs/dbus-glib x11-libs/gtk+:2 
build @ dev-perl/ExtUtils-Depends dev-perl/ExtUtils-PkgConfig dev-perl/Glib
"""

def configure():
    conf("--libexecdir=/usr/lib/xfce4",
            "--disable-static",
            "--disable-gtk-doc",
            '--with-perl-options=INSTALLDIRS="vendor"',
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
