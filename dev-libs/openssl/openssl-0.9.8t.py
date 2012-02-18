metadata = """
summary @ The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
homepage @ http://www.openssl.org
license @ BSD
src_url @ http://www.openssl.org/source/$fullname.tar.gz
arch @ ~x86
slot @ 0.9.8
"""

depends = """
runtime @ dev-lang/perl sys-apps/gawk
build @ x11-misc/makedepend
conflict @ dev-libs/openssl:0
"""

def prepare():
    patch("no-rpath.patch")
    patch("ca-dir.patch")
    patch("%s/openssl-0.9.8m-binutils.patch" % slot, level=1)

def configure():
    system("./Configure --prefix=/usr --openssldir=/etc/ss \
            --libdir=lib shared zlib enable-md2 linux-elf \
            -Wa,--noexecstack %s %s" % (get_env('CFLAGS'), get_env('LDFLAGS')))

def build():
    make("depend")
    make(j=1)
    make("rehash")

def install():
    raw_install("INSTALL_PREFIX=%s MANDIR=%s install" % (install_dir, "/usr/share/man"))
    rmfile("/usr/share/man/man1/passwd.1")
    rmfile("/usr/share/man/man3/threads.3")
    insdoc("LICENSE")
