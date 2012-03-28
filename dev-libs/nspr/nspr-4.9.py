metadata = """
summary @ Netscape Portable Runtime
homepage @ http://www.mozilla.org/projects/nspr/
license @ MPL + GPL
src_url @ ftp://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$version/src/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    system("unset CFLAGS")
    system("unset CXXFLAGS")
    system("./mozilla/nsprpub/configure \
            --prefix=/usr \
            --libdir=/usr/lib \
            --includedir=/usr/include/nspr \
            --enable-optimize \
            --disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/nspr.pc.in" % filesdir, "/usr/lib/pkgconfig/nspr.pc")
