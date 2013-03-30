metadata = """
summary @ GStreamer Bad Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/$name/$fullname.tar.xz
arch @ ~x86_64
options @ orc
slot @ 1
"""

depends = """
common @ media-libs/gstreamer:1 media-plugins/gst-plugins-base:1 sys-libs/glib
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
