metadata = """
summary @ Terminal for XFCE4
license @ GPL-2
homepage @ http://www.xfce.org
src_url @ http://archive.xfce.org/src/apps/$name/0.4/Terminal-$version.tar.bz2
options @ debug dbus
"""

depends = """
runtime @ x11-libs/gtk+ sys-libs/glib x11-libs/libX11 x11-libs/vte xfce-base/exo
build @ dev-util/intltool dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
dbus @ dev-libs/dbus-glib
"""

srcdir = "Terminal-%s" % version

def configure():
    conf("--libexecdir=/usr/lib/xfce4",
    "--disable-static",
    config_enable("dbus"),
    config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

