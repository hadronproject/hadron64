metadata = """
summary @ GStreamer Multimedia Framework
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @  http://gstreamer.freedesktop.org/src/gstreamer/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libxml2 sys-libs/glib
build @ dev-util/intltool
"""

def configure():
    conf(
    '--prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib \
--with-package-name="GStreamer (Hadron GNU/Linux)" \
--with-package-origin="http://www.hadronproject.org/" \
--disable-gtk-doc --disable-static')

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
