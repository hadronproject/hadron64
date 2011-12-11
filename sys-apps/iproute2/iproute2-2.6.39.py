metadata = """
summary @ IP Routing Utilities
homepage @ http://www.linux-foundation.org/en/Net:Iproute2
license @ GPL-2
src_url @ http://www5.frugalware.org/packages/linuxfromscratch/ftp/lfs-packages/7.0-rc2/$fullname.tar.gz
arch @ ~x86
options @ berkdb
"""

#TODO: add atm option

depends = """
runtime @ sys-libs/glibc sys-devel/bison sys-devel/flex >=sys-kernel/linux-api-headers-2.6.27
"""

opt_runtime = """
berkdb @ sys-libs/db
"""

def prepare():
    patch(level=1)
    if not opt("berkdb"):
        sed(""" -i '/^TARGETS=/s: arpd : :' misc/Makefile""")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("mkdir %s/sbin" % install_dir)
    system("ln -s /usr/sbin/ip %s/sbin/ip" % install_dir)
    insfile("include/libnetlink.h", "/usr/include/")
    insfile("lib/libnetlink.a", "/usr/lib/")
    if opt("berkdb"):
        system("mkdir -p %s/var/lib/arpd" % install_dir)
