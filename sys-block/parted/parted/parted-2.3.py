metadata = """
summary @ A program for creating, destroying, resizing, checking and copying partitions
homepage @ http://www.gnu.org/software/parted/parted.html
license @ GPL3
src_url @ http://ftp.gnu.org/gnu/parted/$fullname.tar.gz
options @ device-mapper
arch @ ~x86_64
"""

depends = """
runtime @ sys-fs/e2fsprogs sys-fs/lvm
"""

def configure():
    conf("--enable-device-mapper",
    "--disable-debug \
            --disable-rpath \
            --disable-Werror")

def install():
    raw_install("DESTDIR=%s" % install_dir)
