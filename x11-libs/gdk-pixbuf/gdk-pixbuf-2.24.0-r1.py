metadata = """
summary @ An image loading library for GTK+ V2
homepage @ http://www.gtk.org/
license @ GPL2
src_url @ http://download.gnome.org/sources/gdk-pixbuf/2.24/$fullname.tar.bz2
arch @ ~x86
options @ debug introspection X jpeg tiff
"""

depends = """
runtime @ sys-libs/glib media-libs/libpng
build @ dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
jpeg @ media-libs/jpeg
X @ x11-libs/libX11
tiff @ media-libs/tiff
introspection @ dev-libs/gobject-introspection
"""

def prepare():
    patch("gdk-pixbuf-2.21.4-fix-automagic-x11.patch")
    sed("-i -e 's:libpng15:libpng libpng15:' configure.ac")
    libtoolize(); autoreconf()

def configure():
    export("HOME", build_dir)
    myconf = ""
    if opt("debug"):
        myconf += " --enable-debug=yes "

    conf(
    "--without-libjasper",
    "--with-included-loaders=png",
    "--with-libpng",
    config_with("jpeg", "libjpeg"),
    config_with("tiff", "libtiff"),
    config_with("X", "x11"),
    config_enable("introspection"), myconf)


def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING", "AUTHORS")

def post_install():
    system("/usr/bin/gdk-pixbuf-query-loaders --update-cache")
