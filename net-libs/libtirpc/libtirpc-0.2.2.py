metadata = """
summary @ Transport Independent RPC library (SunRPC replacement)
homepage @ http://libtirpc.sourceforge.net/
license @ BSD
src_url @ http://downloads.sourceforge.net/sourceforge/libtirpc/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
common @ net-libs/libgssglue
"""

def prepare():
    patch(level=1)
    system("sh autogen.sh")
    autoreconf("-fisv")

def configure():
    conf("--enable-gss")

def install():
    installd()
    insfile("doc/etc_netconfig", "/etc/netconfig")
    insfile("COPYING", "/usr/share/licenses/%s/LICENSE" % name)
