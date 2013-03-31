metadata = """
summary @ GStreamer Multimedia Framework Base Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gst-plugins-base/$fullname.tar.xz
arch @ ~x86_64
options @ alsa introspection ogg pango theora vorbis X orc
slot @ 1
"""

depends = """
common @ media-libs/gstreamer:1
build @ dev-util/pkg-config dev-util/gtk-doc
"""

opt_build = """
orc @ dev-lang/orc
"""

opt_common = """
alsa @ media-libs/alsa-lib
introspection @ dev-libs/gobject-introspection
ogg @ media-libs/libogg
pango @ media-libs/pango
theora @ media-libs/libtheora[encode]
vorbis @ media-libs/libvorbis
X @ x11-libs/libX11 x11-libs/libXext x11-libs/libXv
"""

def configure():
    sed("-i '/AC_PATH_XTRA/d' configure.ac")
    system('aclocal -I m4 -I common/m4')
    autoconf()
    automake('--add-missing')
    conf('--disable-static',
         '--enable-experimental',
         '--disable-gnome_vfs',
         '--with-package-name="GStreamer Base Plugins (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"',
         config_enable('alsa'),
         config_enable('introspection'),
         config_enable('ogg'),
         config_enable('pango'),
         config_enable('theora'),
         config_enable('vorbis'),
         config_enable('X'))

def build():
    make()
    system("sed -e 's/^SUBDIRS_EXT =.*/SUBDIRS_EXT =/' -i Makefile")

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
    raw_install("-C ext DESTDIR=%s" % install_dir)
    raw_install("-C gst-libs DESTDIR=%s" % install_dir)
