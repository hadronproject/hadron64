metadata = """
summary @ Gnome Configuration System and Daemon
homepage @ http://projects.gnome.org/gconf/
license @ LGPL2
src_url @ http://ftp.gnome.org/pub/gnome/sources/GConf/2.32/GConf-$version.tar.bz2
arch @ ~x86_64
options @ debug policykit
"""

depends = """
runtime @ gnome-base/orbit dev-libs/libxml2 sys-apps/dbus x11-libs/gtk+:2 
build @ dev-libs/gobject-introspection
"""

opt_build = """
policykit @ sys-auth/polkit
"""

srcdir = "GConf-%s" % version

def prepare():
    patch(level=1)

def configure():
    conf("--enable-gtk",
            "--disable-static",
            "--enable-gsettings-backend",
            "--with-gtk=2.0",
            "--without-openldap",
            config_enable("policykit", "defaults-service"),
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS")
    makedirs("/etc/gconf/gconf.xml.system")
    insexe("%s/gconf-merge-schema" % filesdir, "/usr/bin/gconf-merge-schema")
    insexe("%s/gconfpkg" % filesdir, "/usr/sbin/gconfpkg")

def post_install():
    system("ldconfig -r /")
    setmod("755 /etc/gconf/gconf.xml.system")
    system("/usr/bin/gio-querymodules /usr/lib/gio/modules")
