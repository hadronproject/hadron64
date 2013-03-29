metadata = """
summary @ GStreamer Bad Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/$name/$fullname.tar.xz
arch @ ~x86_64
options @ orc
"""

depends = """
common @ media-libs/gstreamer media-plugins/gst-plugins-base sys-libs/glib
"""

opt_build = """
orc @ dev-lang/orc
"""

def configure():
    conf('--disable-examples',
         '--disable-debug',
         '--with-package-name="GStreamer Bad Plugins (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"',
         config_enable('orc'))

def install():
    raw_install("DESTDIR=%s" % install_dir)
