metadata = """
summary @ GNU database library
homepage @ http://www.gnu.org/software/gdbm/gdbm.html
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)

def configure():
    conf("--enable-libgdbm-compat --disable-static")

def install():
    linstall()
    makedirs("/usr/include/gdbm")
    makesym("../gdbm.h", "/usr/include/gdbm/gdbm.h")
    makesym("../ndbm.h", "/usr/include/gdbm/ndbm.h")
    makesym("../dbm.h", "/usr/include/gdbm/dbm.h")
    #raw_install("INSTALL_ROOT=%s" % install_dir)
    #raw_install("INSTALL_ROOT=%s includedir=/usr/include/gdbm" % install_dir, "install-compat")
