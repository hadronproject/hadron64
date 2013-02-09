metadata = """
summary @ The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
homepage @ http://www.openssl.org
license @ BSD
src_url @ http://www.openssl.org/source/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl sys-apps/gawk
"""

#def prepare():
    #patch("openssl-1.0.1-x32.patch", level=1)
    #patch("openssl-1.0.1-ipv6.patch")
    #    patch("fix-manpages.patch", level=1)
#    patch("no-rpath.patch")
#    patch("ca-dir.patch")
#    patch("openssl-1.0.0d-fbsd-amd64.patch")
#    patch("openssl-1.0.0d-windres.patch")


def configure():
    if not system("./Configure --prefix=/usr --openssldir=/etc/ssl \
            --libdir=lib shared zlib enable-md2 linux-x86_64 enable-ec_nistp_64_gcc_128 \
            -Wa,--noexecstack %s %s" % (get_env('CFLAGS'), get_env('LDFLAGS'))):
        raise BuiltinError("openssl-%s configure failed." % version)

def build():
    make("depend")
    make("all", j=1)
    make("rehash")

def install():
    raw_install("INSTALL_PREFIX=%s MANDIR=%s install" % (install_dir, "/usr/share/man"))
    insdoc("LICENSE")
