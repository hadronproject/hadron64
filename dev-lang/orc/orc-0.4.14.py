metadata = """
summary @ The Oil Runtime Compiler
homepage @ http://code.entropywave.com/projects/orc/
license @ BSD BSD-2
src_url @ http://code.entropywave.com/download/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    "--prefix=/usr --disable-static")

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
