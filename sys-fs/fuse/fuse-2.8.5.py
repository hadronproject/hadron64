metadata = """
summary @ A library that makes it possible to implement a filesystem in a userspace program.
homepage @ http://fuse.sourceforge.net/
license @ GPL2
src_url @ http://downloads.sourceforge.net/fuse/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf("--enable-lib",
            "--enable-util",
            "--bindir=/bin")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    rmdir("/dev")

    rmdir("/etc/init.d")

    makedirs("/lib")

    move("/usr/lib/libfuse.so.%s" % version, "/lib/libfuse.so.%s" % version)
    makesym("/lib/libfuse.so.%s" % version, "/usr/lib/libfuse.so.%s" % version)
    makesym("libfuse.so.%s" % version, "/lib/libfuse.so.2")

    move("/usr/lib/libulockmgr.so.1.0.1", "/lib/libulockmgr.so.1.0.1")
    makesym("/lib/libulockmgr.so.1.0.1", "/usr/lib/libulockmgr.so.1.0.1")
    makesym("libulockmgr.so.1.0.1", "/lib/libulockmgr.so.1")

    insfile("%s/fuse.conf" % filesdir, "/etc/fuse.conf")

    move("/etc/udev", "/lib/udev")
