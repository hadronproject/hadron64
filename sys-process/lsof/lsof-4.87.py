metadata = """
summary @ Lists open files for running Unix processes
homepage @ http://people.freebsd.org/~abe/
license @ lsof
src_url @ ftp://download.tuxfamily.org/hadron/distfiles/$name_$version_src.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir="%s_%s_src"  % (name,version)

def configure():
    sed("-i 's|/\* #define\tHASSECURITY\t1 \*/|#define\tHASSECURITY\t1|' \
        dialects/linux/machine.h")
    system("./Configure -n linux")

def install():
    insexe("lsof", "/usr/sbin/lsof")
    insdoc("00CREDITS", "00DCACHE", "00DIALECTS", "00DIST", "00FAQ", \
           "00LSOF-L", "00MANIFEST", "00PORTING", "00QUICKSTART", "00README", \
           "00.README.FIRST", "00TEST", "00XCONFIG")
    insinto("lsof.8", "/usr/share/man/man8/lsof.8")
