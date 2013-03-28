metadata = """
summary @ An image loading library for GTK+ V2
homepage @ http://www.gtk.org/
license @ GPL2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.26/gdk-pixbuf-$version.tar.xz
arch @ ~x86_64
options @ debug introspection X jpeg tiff
"""

depends = """
runtime @ sys-libs/glib media-libs/libpng
build @ dev-util/pkg-config sys-devel/gettext
"""

opt_common = """
jpeg @ media-libs/jpeg
X @ x11-libs/libX11
tiff @ media-libs/tiff
introspection @ dev-libs/gobject-introspection
"""

def configure():
    export("HOME", build_dir)
    myconf = ""
    if opt("debug"):
        myconf += " --enable-debug=yes "

    conf(
    "--without-libjasper",
    "--with-included-loaders=png",
    "--with-libpng",
    config_enable("introspection"),
    config_with("jpeg", "libjpeg"),
    config_with("tiff", "libtiff"),
    config_with("X", "x11"), myconf)


def build():
    export("HOME", build_dir)
    if opt("introspection"): unset_env_variables()
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING", "AUTHORS")

def post_install():
    if not system("/usr/bin/gdk-pixbuf-query-loaders --update-cache"):
        raise BuildError
