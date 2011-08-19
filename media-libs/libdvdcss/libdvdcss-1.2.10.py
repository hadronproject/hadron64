metadata = """
summary @ A portable abstraction library for DVD decryption
homepage @ http://www.videolan.org/libdvdcss
license @ GPL
src_url @ http://download.videolan.org/pub/libdvdcss/$version/$fullname.tar.bz2
arch @ ~x86
options @ doc
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_build = """
doc @ app-doc/doxygen
"""

def configure():
    conf(
    "--enable-static",
    "--enable-shared",
    config_enable("doc"),
    "--disable-dependency-tracking")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")

    if opt("doc"):
        insdoc("doc/latex/refman.ps")
