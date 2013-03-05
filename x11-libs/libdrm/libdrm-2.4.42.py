metadata = """
summary @ Userspace interface to kernel DRM services
homepage @ http://dri.freedesktop.org/
license @ MIT
src_url @ http://dri.freedesktop.org/libdrm/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/perl[ithreads] sys-devel/libtool x11-libs/libpciaccess
"""

def prepare():
    patch(level=1)

def configure():
    autoreconf("--force --install")
    conf("--enable-udev",
      "--enable-omap-experimental-api",
      "--enable-exynos-experimental-api")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    # This is no good.
    copy("%s/COPYING" % filesdir, build_dir, ignore_fix_target=True)
    insdoc("COPYING")
