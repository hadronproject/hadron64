metadata = """
summary @ Userspace interface to kernel DRM services
homepage @ http://dri.freedesktop.org/
license @ MIT
src_url @ http://dri.freedesktop.org/libdrm/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/perl[ithreads] sys-devel/libtool
"""

def prepare():
    patch(level=1)

def configure():
    autoreconf("--force --install")
    conf(
    "--prefix=/usr",
    "--enable-udev",
    "--enable-intel",
    "--enable-radeon",
    "--enable-vmwgfx-experimental-api",
    "--enable-nouveau-experimental-api")

def install():
    raw_install("DESTDIR=%s" % install_dir)
