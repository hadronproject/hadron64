metadata = """
summary @ Utilities for rescue and embedded systems
homepage @ http://busybox.net
license @ GPL
src_url @ http://busybox.net/downloads/$fullname.tar.bz2
arch @ ~x86_64
"""

def prepare():
    copy("%s/config" % filesdir, ".config")

def install():
    makedirs("/bin")

    insexe("busybox", "/bin/busybox")
