metadata = """
summary @ Tools for managing Linux kernel modules
homepage @ http:/kerneltools.org
license @ GPL-2
src_url @ http://www.kernel.org/pub/linux/utils/kernel/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """ 
runtime @ sys-libs/glibc
"""

def prepare():
    echo(".so man5/modprobe.conf.5", "modprobe.d.5")

def configure():
    conf("--exec-prefix=/",
        "--enable-zlib")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    system("mkdir -p %s/etc/modprobe.d" % install_dir)
    #insfile("%s/modprobe.conf" % filesdir, "%s/etc/modprobe.d/modprobe.conf" % install_dir)
    insinto("%s/*" % filesdir, "%s/etc/modprobe.d" % install_dir)

