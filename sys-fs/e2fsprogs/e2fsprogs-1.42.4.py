metadata = """
summary @ Ext2/3/4 filesystem utilities
homepage @ http://e2fsprogs.sourceforge.net/
license @ MIT + GPL + LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/e2fsprogs/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-apps/util-linux app-shells/bash
"""

def configure():
    raw_configure("--enable-elf-shlibs",
            "--disable-fsck", "--disable-uuidd",
            "--disable-libuuid", "--disable-libblkid")

def install():
    raw_install("install install-libs LDCONFIG=/bin/true \
            DESTDIR=%s root_sbindir=/sbin root_libdir=/lib" % install_dir)

    sed(""" -i -e 's#^SS_DIR=.*#SS_DIR="/usr/share/ss"#' "%s/usr/bin/mk_cmds" """ % install_dir)
    sed(""" -i -e 's#^ET_DIR=.*#ET_DIR="/usr/share/et"#' "%s/usr/bin/compile_et" """ % install_dir)

