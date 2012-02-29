metadata = """
summary @ Miscellaneous system utilities for Linux
homepage @ http://userweb.kernel.org/~kzak/util-linux-ng/
license @ GPL-2
src_url @ ftp://ftp.kernel.org/pub/linux/utils/$name/v$version/$fullname.tar.bz2
arch @ ~x86
"""

# FIXME: add some options and dependencies

depends = """
runtime @ sys-apps/baselayout
"""

def prepare():
    patch(level=1)

def configure():
    sed("-e 's@etc/adjtime@var/lib/hwclock/adjtime@g' \
            -i $(grep -rl '/etc/adjtime' .)")
    conf("--enable-arch",
        "--enable-write",
        "--enable-partx",
        "--disable-wall",
        "--enable-libmount-mount",
        "--enable-raw")

def install():
    makedirs("/var/lib/hwclock")
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "NEWS", "README*", "docs/*")
