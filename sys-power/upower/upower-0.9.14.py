metadata = """
summary @ Abstraction for enumerating power devices, listening to device events and querying history and statistics
homepage @ http://upower.freedesktop.org
license @ GPL
src_url @ http://upower.freedesktop.org/releases/$fullname.tar.bz2
arch @ ~x86
options @ introspection
"""

depends = """
common @ >=dev-libs/dbus-glib-0.88 >=sys-libs/glib-2.21.5 sys-apps/dbus >=sys-auth/polkit-0.101
build @ dev-libs/libxslt app-text/docbook-xsl-stylesheets >=dev-util/intltool-0.40.0 dev-util/pkg-config
>=sys-power/pm-utils-1.4.1 >=sys-fs/udev-151[extras]
"""

opt_runtime = """
introspection @ dev-libs/gobject-introspection
"""

def configure():
    autoreconf("-fi")
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--localstatedir=/var",
            "--libexecdir=/usr/lib/upower",
            "--disable-static",
            "--disable-man-pages",
            "--disable-gtk-doc",
            "--disable-tests",
            config_enable("introspection"),
            config_enable("debug", "verbose-mode"))

def build():
    # For g-i-r
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("ChangeLog", "COPYING", "README", "HACKING", "NEWS")
