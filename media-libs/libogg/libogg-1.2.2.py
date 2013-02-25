metadata = """
summary @ Ogg bitstream and framing library
homepage @ http://www.xiph.org/ogg/
license @ BSD
src_url @ http://downloads.xiph.org/releases/ogg/$fullname.tar.gz
arch @ ~x86_64
options @ static-libs
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    "--disable-dependency-tracking",
    config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "CHANGES")
