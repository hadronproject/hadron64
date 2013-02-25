metadata = """
summary @ library for id3 tagging
homepage @ http://www.underbit.com/products/mad/
license @ GPL
src_url @ ftp://ftp.mars.org/pub/mpeg/$name-$versionb.tar.gz
arch @ ~x86_64
options @ static-libs debug
"""

depends = """
runtime @ sys-libs/zlib
build @ dev-util/gperf
"""

srcdir = fullname + "b"

def prepare():
    patch("10_utf16.patch", level=1)
    patch("11_unknown_encoding.patch", level=1)
    patch("CVE-2008-2109.patch")

def configure():
    conf(
    config_enable("static-libs", "static"),
    config_enable("debug", "debugging"))


def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("mkdir %s/usr/lib/pkgconfig -p" % install_dir)
    insfile("%s/id3tag.pc" % filesdir, "/usr/lib/pkgconfig/id3tag.pc")
