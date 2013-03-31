metadata = """
summary @ GStreamer Good Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/$name/$fullname.tar.xz
arch @ ~x86_64
options @ orc
slot @ 1
"""

depends = """
common @ media-libs/gstreamer:1 media-plugins/gst-plugins-base:1 sys-libs/glib
   app-arch/bzip2 sys-libs/zlib
build @ dev-util/gtk-doc
"""

opt_build = """
orc @ dev-lang/orc
"""

def configure():
    conf('--enable-bz2',
         '--enable-zlib',
         '--disable-examples',
         '--with-default-audiosink=autoaudiosink',
         '--with-default-visualizer=goom',
         '--with-package-name="GStreamer Good Plugins (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"',
         config_enable('orc'))

def install():
    raw_install("DESTDIR=%s" % install_dir)
