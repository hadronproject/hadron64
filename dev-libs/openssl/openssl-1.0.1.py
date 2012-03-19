metadata = """
summary @ The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
homepage @ http://www.openssl.org
license @ BSD
src_url @ http://www.openssl.org/source/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl sys-apps/gawk
build @ x11-misc/makedepend
"""

def prepare():
    patch("fix-manpages.patch", level=1)
    patch("no-rpath.patch")
    patch("ca-dir.patch")
    patch("openssl-1.0.0d-fbsd-amd64.patch")
    patch("openssl-1.0.0d-windres.patch")


def configure():
    if not system("./Configure --prefix=/usr --openssldir=/etc/ss \
            --libdir=lib shared zlib enable-md2 linux-elf \
            -Wa,--noexecstack %s %s" % (get_env('CFLAGS'), get_env('LDFLAGS'))):
        raise BuiltinError("openssl-%s configure failed." % version)

def build():
    make("depend")
    make(j=1)
    make("rehash")

def install():
    raw_install("INSTALL_PREFIX=%s MANDIR=%s install" % (install_dir, "/usr/share/man"))
    insdoc("LICENSE")
