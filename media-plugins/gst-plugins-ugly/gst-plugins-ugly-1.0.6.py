metadata = """
summary @ GStreamer Ugly Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gst-plugins-ugly/$fullname.tar.xz
arch @ ~x86_64
options @ orc
slot @ 1
"""

depends = """
build @ dev-util/pkg-config 
common @ media-plugins/gst-plugins-base:1 media-sound/lame media-libs/libmpeg2
    media-libs/libmad media-libs/a52dec media-libs/libid3tag dev-libs/libcdio
    media-libs/libdvdread media-libs/opencore-amr media-libs/x264
"""

opt_build = """
orc @ dev-lang/orc
"""

def configure():
    conf('--disable-static',
         '--enable-experimental',
         '--with-package-name="GStreamer Ugly Plugins (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"')

def install():
    raw_install("DESTDIR=%s" % install_dir)
    raw_install("-C ext DESTDIR=%s" % install_dir)
