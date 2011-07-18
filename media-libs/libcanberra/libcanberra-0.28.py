metadata = """
summary @ A small and lightweight implementation of the XDG Sound Theme Specification
homepage @ http://0pointer.de/lennart/projects/libcanberra
license @ LGPL
src_url @ http://0pointer.de/lennart/projects/libcanberra/$fullname.tar.gz
arch @ ~x86
options @ gstreamer gtk alsa udev tdb
"""

depends = """
runtime @ media-libs/libvorbis sys-devel/libtool
"""

opt_runtime = """
gstreamer @ media-libs/gstreamer 
gtk @ x11-libs/gtk+
alsa @ media-libs/alsa-lib
    udev @ sys-fs/udev
tdb @ dev-db/tdb
"""

def configure():
	conf(
	"--sysconfdir=/etc --prefix=/usr --localstatedir=/var \
      --disable-static --with-builtin=dso --enable-null --disable-oss \
      --disable-pulse \
      --with-systemdsystemunitdir=/lib/systemd/system",
      config_enable("gstreamer"),
      config_enable("gtk"),
      config_enable("tdb"),
      config_enable("udev"),
      config_enable("alsa"))

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING")

