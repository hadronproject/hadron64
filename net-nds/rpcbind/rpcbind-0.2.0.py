metadata = """
summary @ portmap replacement which supports RPC over various protocols
homepage @ http://sourceforge.net/projects/rpcbind/
license @ BSD
src_url @ http://downloads.sourceforge.net/sourceforge/rpcbind/$fullname.tar.bz2
arch @ ~x86_64
"""

prepare = lambda: patch(level=1)

depends = """
common @ net-libs/libtirpc
"""

def configure():
    conf("--enable-warmstarts --with-statedir=/run")

def install():
    installd()
    insfile("man/rpcinfo.8", "/usr/share/man/man8/rpcinfo.8")
    insfile("%s/rpcbind" % filesdir,  "/etc/rc.d/rpcbind")
    insdoc("COPYING")
