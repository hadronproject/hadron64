metadata = """
summary @ C library that performs DNS requests and name resolves asynchronously
homepage @ http://c-ares.haxx.se/
license @ custom
src_url @ http://c-ares.haxx.se/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    "--enable-shared",
"--enable-nonblocking",
"--enable-symbol-hiding")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("RELEASE-NOTES", "CHANGES", "NEWS")
