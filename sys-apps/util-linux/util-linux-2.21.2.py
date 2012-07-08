metadata = """
summary @ Miscellaneous system utilities for Linux
homepage @ http://userweb.kernel.org/~kzak/util-linux-ng/
license @ GPL-2
src_url @ ftp://ftp.kernel.org/pub/linux/utils/$name/v2.21/$name-2.21.tar.xz
arch @ ~x86_64
"""

# FIXME: update, add options and dependencies

#depends = """
#runtime @ sys-apps/baselayout
#"""

srcdir = "%s-2.21" % name

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
    insdoc("AUTHORS", "NEWS", "README*", "TODO", "docs/*")
