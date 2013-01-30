metadata = """
summary @ IP Routing Utilities
homepage @ http://www.linux-foundation.org/en/Net:Iproute2
license @ GPL-2
src_url @ http://www.kernel.org/pub/linux/utils/net/$name/$name-$version.tar.xz
arch @ ~x86_64
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
    #patch(level=1)
    if not opt("berkdb"):
        sed("-i '/^TARGETS/s@arpd@@g' misc/Makefile")
        sed("-i /ARPD/d Makefile")
        sed("-i 's/arpd.8//' man/man8/Makefile")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("include/libnetlink.h", "/usr/include/")
    insfile("lib/libnetlink.a", "/usr/lib/")
    if opt("berkdb"):
        makedirs("/var/lib/arpd")
