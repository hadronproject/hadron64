metadata = """
summary @ D-Bus interface for user account query and manipulation
homepage @ http://cgit.freedesktop.org/accountsservice/
license @ GPL3
src_url @ http://cgit.freedesktop.org/accountsservice/snapshot/$name-$version.tar.bz2
arch @ ~x86_64
options @ introspection
"""

depends = """
runtime @ dev-libs/dbus-glib sys-auth/polkit
build @ dev-util/intltool dev-libs/libxslt dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
introspection @ dev-libs/gobject-introspection
"""

def configure():
    system("./autogen.sh")
    conf(
    "--libexecdir=/usr/lib/accountsservice",
    "--with-systemdsystemunitdir=/lib/systemd/system",
    "--disable-docbook-docs",
    "--disable-maintainer-mode",
    "--disable-more-warnings",
    "--localstatedir=/var",
    "--disable-static",
    config_enable("introspection"))


def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "NEWS", "README", "TODO")
