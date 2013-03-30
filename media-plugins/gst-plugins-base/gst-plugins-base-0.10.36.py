metadata = """
summary @ GStreamer Multimedia Framework Base Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gst-plugins-base/$fullname.tar.bz2
arch @ ~x86_64
slot @ 0
"""

depends = """
build @ media-libs/gstreamer:0 x11-libs/libXv media-libs/alsa-lib media-libs/libvorbis media-libs/pango
        dev-libs/gobject-introspection dev-util/pkg-config dev-lang/orc
"""

def configure():
    sed("-i 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac")
    system("sed -i '/AC_PATH_XTRA/d' configure.ac")
    system('aclocal -I m4 -I common/m4')
    autoconf()
    automake('--add-missing')
    conf(
    '--prefix=/usr --sysconfdir=/etc --localstatedir=/var \
    --disable-static --enable-experimental --disable-gnome_vfs \
    --with-package-name="GStreamer Base Plugins (Hadron GNU/Linux)" \
    --with-package-origin="http://www.hadronproject.org/"')

def build():
    make()
    system("sed -e 's/^SUBDIRS_EXT =.*/SUBDIRS_EXT =/' -i Makefile")

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
    raw_install("-C ext DESTDIR=%s" % install_dir)
    raw_install("-C gst-libs DESTDIR=%s" % install_dir)
