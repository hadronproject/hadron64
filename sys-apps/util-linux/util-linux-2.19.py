metadata = """
summary @ Miscellaneous system utilities for Linux
homepage @ http://userweb.kernel.org/~kzak/util-linux-ng/
license @ GPL-2
src_url @ ftp://ftp.kernel.org/pub/linux/utils/$name/v2.19/$fullname.tar.bz2
arch @ ~x86
"""

# FIXME: update, add options and dependencies

def configure():
    system("sed -e 's@etc/adjtime@var/lib/hwclock/adjtime@g' \
            -i $(grep -rl '/etc/adjtime' .)")
    #system("sed -e 's%etc/adjtime%var/lib/hwclock/adjtime%' -i hwclock/hwclock.c")
    conf("--enable-arch",
        "--enable-write",
        "--enable-partx",
        "--disable-use-tty-group")

def install():
    makedirs("/var/lib/hwclock")
    raw_install("DESTDIR=%s install" % install_dir)
