metadata = """
summary @ The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
homepage @ http://www.openssl.org
license @ BSD
src_url @ http://www.openssl.org/source/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl sys-apps/gawk
"""

def prepare():
    patch("fix-manpages.patch", level=1)
    patch("no-rpath.patch")
    patch("ca-dir.patch")

def configure():
    system("./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib shared zlib enable-md2 -Wa,--noexecstack")

def build():
    make("depend")
    make(j=1)
    make("rehash")

def install():
    raw_install("INSTALL_PREFIX=%s MANDIR=%s install" % (install_dir, "/usr/share/man"))
