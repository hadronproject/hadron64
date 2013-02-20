metadata = """
summary @ System Utilities Based on Sysfs
homepage @ http://linux-diag.sourceforge.net/Sysfsutils.html
license @ GLP LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/linux-diag/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

import glob

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makedirs("/lib")

    for l in glob.glob("%s/usr/lib/libsysfs.so.2*" % install_dir):
        move(l, "/lib/%s" % basename(l))
    rmfile("/usr/lib/libsysfs.so")
    makesym("/lib/libsysfs.so.2", "/usr/lib/libsysfs.so")
