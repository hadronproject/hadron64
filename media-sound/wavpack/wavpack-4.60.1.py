metadata = """
summary @ Audio compression format with lossless, lossy, and hybrid compression modes
homepage @ http://www.wavpack.com/
license @ custom
src_url @ http://www.wavpack.com/$fullname.tar.bz2
arch @ ~x86_64
options @ mmx
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    "--disable-static",
    config_enable("mmx"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("license.txt")
