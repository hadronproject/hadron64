metadata = """
summary @ A free library for decoding ATSC A/52 streams
homepage @ http://liba52.sourceforge.net/
license @ GPL2
src_url @ http://liba52.sourceforge.net/files/$name-$version.tar.gz
arch @ ~x86
options @ djbfft static-libs
"""

opt_runtime = """
djbfft @ sci-libs/djbfft
"""

def prepare():
    patch("a52dec-0.7.4-build.patch",level=1)
    autoreconf("-fi")

def configure():
    raw_configure("--prefix=/usr",
                "--enable-shared",
                config_enable("static-libs", "static"),
                config_enable("djbfft"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("liba52/a52_internal.h", "/usr/include/a52dec/a52_internal.h")
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "doc/liba52.txt")
