metadata = """
summary @ Virtual Terminal Emulator widget for use with
homepage @ http://www.gnome.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/GNOME/sources/vte/0.28/$fullname.tar.bz2
arch @ ~x86
options @ debug introspection
"""

depends = """
build @ dev-util/intltool dev-util/pkg-config sys-devel/gettext
runtime @ x11-libs/libXft x11-libs/libX11 sys-libs/ncurses media-libs/pango sys-libs/glib
"""

opt_runtime = """
introspection @ dev-libs/gobject-introspection
"""

def configure():
    conf("--disable--static",
        "--enable-python",
        config_enable("debug"),
        config_enable("introspection"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    export("HOME", build_dir)
    append_cflags("-fno-strict-aliasing")
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("README")
