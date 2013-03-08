metadata = """
summary @ Geek kernel sources
homepage @ https://github.com/init6/init_6/tree/master/sys-kernel/geek-sources
license @ GPL
src_url @ https://www.kernel.org/pub/linux/kernel/v3.x/linux-$version.tar.bz2
arch @ ~x86_64
options @ aufs bfq fix genpatches ice zen zfs
"""

srcdir = "linux-%s" % version

standard_procedure = False

def prepare():
    if opt("aufs"):
    	patch("aufs", level=1)

    if opt("bfq"):
    	patch("bfq", level=1)

    if opt("fix"):
        patch("fix", level=1)

    if opt("genpatches"):
        patch("genpatches", level=1)

    if opt("ice"):
        patch("ice", level=1)

    if opt("zen"):
        patch("zen", level=1)

    if opt("zfs"):
        patch("zfs", level=1)

def install():
    
    cd("../")
    
    copytree(build_dir, "/usr/src/linux-geek-%s" % version)
