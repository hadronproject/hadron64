metadata = """
summary @ Lists open files for running Unix processes
homepage @ http://people.freebsd.org/~abe/
license @ lsof
src_url @ http://repository.timesys.com/buildsources/l/lsof/lsof-4.85/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    cd("../%s_4.85_src" % name)
    system("sed -i 's|/\* #define\tHASSECURITY\t1 \*/|#define\tHASSECURITY\t1|' \
            dialects/linux/machine.h")
    system("./Configure -n linux")

def build():
    cd("../%s_4.85_src" % name)
    make()

def install():
    cd("../%s_4.85_src" % name)
    insexe("lsof", "/usr/sbin/lsof")
