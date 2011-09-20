metadata = """
summary @ An implementation of basic iCAL protocols from citadel, previously known as aurore
homepage @ http://freeassociation.sourceforge.net
license @ LGPL-2 MPL-2
src_url @ http://downloads.sourceforge.net/freeassociation/$fullname.tar.gz
arch @ ~x86
"""

def configure():
    # FIXME: I must implement a termination command 
    # for lpms to exit on error conditions.
    system("./autogen.sh")
    libtoolize("--force")
    conf("--enable-shared", "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
