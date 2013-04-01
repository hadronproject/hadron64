metadata = """
summary @ GStreamer Multimedia Framework
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gstreamer/$fullname.tar.xz
arch @ ~x86_64
options @ introspection nls
slot @ 1
"""

depends = """
common @ dev-libs/libxml2 sys-libs/glib
build @ dev-util/intltool
"""

opt_build = """
nls @ sys-devel/gettext
"""

opt_common = """
introspection @ dev-libs/gobject-introspection
"""

def configure():
    conf('--disable-static',
         '--disable-gtk-doc',
         '--with-package-name="GStreamer (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"',
         config_enable('introspection'),
         config_enable('nls'))

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
