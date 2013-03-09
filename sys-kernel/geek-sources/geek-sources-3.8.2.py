metadata = """
summary @ Geek kernel sources
homepage @ https://github.com/init6/init_6/tree/master/sys-kernel/geek-sources
license @ GPL
src_url @ https://www.kernel.org/pub/linux/kernel/v3.x/linux-$version.tar.bz2
http://download.tuxfamily.org/hadron/distfiles/$fullname-patches.tar.bz2
arch @ ~x86_64
options @ bfq fix genpatches ice zen zfs
"""

srcdir = "linux-%s" % version

standard_procedure = False

def prepare():

    for bu in ("bfq", "fix", "genpatches", "ice", "zen", "zfs"):
        if opt(bu):
            patch(bu, location="%s" % dirname(build_dir), level=1)

def install():
    
    cd("../")
    
    copytree(build_dir, "/usr/src/linux-geek-%s" % version)
