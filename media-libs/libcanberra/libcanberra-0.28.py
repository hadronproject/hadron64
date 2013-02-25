metadata = """
summary @ A small and lightweight implementation of the XDG Sound Theme Specification
homepage @ http://0pointer.de/lennart/projects/libcanberra
license @ LGPL
src_url @ http://0pointer.de/lennart/projects/libcanberra/$fullname.tar.gz
arch @ ~x86_64
options @ gstreamer gtk alsa udev tdb gtk3
"""

depends = """
runtime @ media-libs/libvorbis sys-devel/libtool
"""

opt_runtime = """
gstreamer @ media-libs/gstreamer
gtk @ x11-libs/gtk+:2 gnome-base/gconf
alsa @ media-libs/alsa-lib
    udev @ sys-fs/udev
tdb @ dev-db/tdb
gtk3 @ x11-libs/gtk+:3 gnome-base/gconf
"""

def configure():
    conf(
    "--sysconfdir=/etc --prefix=/usr --localstatedir=/var",
    "--disable-static --with-builtin=dso --enable-null --disable-oss",
    "--disable-pulse",
    "--with-systemdsystemunitdir=/lib/systemd/system",
    "--disable-dependency-tracking",
    config_enable("gtk3"),
    config_enable("gstreamer"),
    config_enable("gtk"),
    config_enable("tdb"),
    config_enable("udev"),
    config_enable("alsa"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
