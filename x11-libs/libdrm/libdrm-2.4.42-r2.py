metadata = """
summary @ Userspace interface to kernel DRM services
homepage @ http://dri.freedesktop.org/
license @ MIT
src_url @ http://dri.freedesktop.org/libdrm/$fullname.tar.bz2
arch @ ~x86_64
options @ exynos intel nouveau radeon vmware
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/perl[ithreads] sys-devel/libtool
"""

opt_common = """
intel @ >=x11-libs/libpciaccess-0.10
"""

def prepare():
    patch(level=1)

def configure():
    autoreconf("--force --install")
    conf("--enable-udev",
            config_enable("intel"),
            config_enable("nouveau"),
            config_enable("radeon"),
            config_enable("vmware", "vmwgfx"),
            config_enable("exynos", "exynos-experimental-api"),
            config_enable("omap", "omap-experimental-api"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    # This is no good.
    copy("%s/COPYING" % filesdir, build_dir)
    insdoc("COPYING")
