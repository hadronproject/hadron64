metadata = """
summary @ GStreamer Ugly Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gst-plugins-ugly/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ dev-util/pkg-config media-plugins/gst-plugins-base media-sound/lame media-libs/libmpeg2
    media-libs/libmad media-libs/a52dec media-libs/libid3tag dev-libs/libcdio media-libs/libdvdread
    media-libs/opencore-amr media-libs/x264
"""

def configure():
    conf(
    '--prefix=/usr --sysconfdir=/etc --localstatedir=/var \
    --disable-static --enable-experimental \
    --with-package-name="GStreamer Ugly Plugins (Hadron GNU/Linux)" \
    --with-package-origin="http://www.hadronproject.org/"')

def install():
    raw_install("DESTDIR=%s" % install_dir)
    raw_install("-C ext DESTDIR=%s" % install_dir)
