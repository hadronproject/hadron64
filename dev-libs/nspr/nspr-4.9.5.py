metadata = """
summary @ Netscape Portable Runtime
homepage @ http://www.mozilla.org/projects/nspr/
license @ MPL + GPL
src_url @ ftp://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$version/src/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    sed("-e 's/\$(MKSHLIB) \$(OBJS)/\$(MKSHLIB) \$(LDFLAGS) \$(OBJS)/g' \
            -i mozilla/nsprpub/config/rules.mk")

def configure():
    if not system("./mozilla/nsprpub/configure \
            --prefix=/usr \
            --libdir=/usr/lib \
            --includedir=/usr/include/nspr \
            --enable-optimize --with-pthreads\
            --disable-debug --enable-64bit --with-mozilla"):
        raise BuildError

def install():
    raw_install("DESTDIR=%s" % install_dir)
    makesym("nspr.pc", "/usr/lib/pkgconfig/mozilla-nspr.pc")
    setmod("644 %s/usr/lib/*.a" % install_dir)
    rmfile("/usr/bin/compile-et.pl")
    rmfile("/usr/bin/prerr.properties")
    rmfile("/usr/share/aclocal/nspr.m4")
    rmdir("/usr/include/nspr/md")

