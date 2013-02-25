metadata = """
summary @ A collection of routines used to create PNG format graphics files (ver 1.2)
homepage @ http://www.libpng.org/pub/png/libpng.html
license @ custom
src_url @ http://pts-mini-gpl.googlecode.com/svn-history/r266/trunk/build-jbig2/libpng-1.2.46.tar.gz
http://garr.dl.sourceforge.net/project/libpng-apng/libpng-devel/1.5.4/libpng-1.5.4-apng.patch.gz
options @ apng
arch @ ~x86_64
slot @ 1.2
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def build():
    make("ECHO=echo")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    cd(install_dir)
    system("rm -fr usr/share")
    system("rm -fr usr/bin/libpng-config")
    system("rm -rf usr/lib/{libpng.so,libpng.a}")
    system("rm -fr usr/lib/pkgconfig/libpng.pc")
    system("rm -rf usr/include/{pngconf.h,png.h}")

