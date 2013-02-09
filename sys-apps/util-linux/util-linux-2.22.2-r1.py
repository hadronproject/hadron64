metadata = """
summary @ Miscellaneous system utilities for Linux
homepage @ http://userweb.kernel.org/~kzak/util-linux-ng/
license @ GPL-2
src_url @ http://ftp.kernel.org/pub/linux/utils/$name/v2.22/$name-2.22.2.tar.xz
arch @ ~x86_64
"""

# TODO:
# * Dependencies 
# * Options
# * More configuration

def configure():
    sed("-e 's@etc/adjtime@var/lib/hwclock/adjtime@g' \
            -i $(grep -rl '/etc/adjtime' .)")
    conf("--enable-arch",
        "--enable-write",
        "--enable-partx",
        "--disable-wall",
        "--disable-su --disable-sulogin --disable-login",
        "--enable-raw")

def install():
    makedirs("/var/lib/hwclock")
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "NEWS", "README*", "TODO", "docs/*")
