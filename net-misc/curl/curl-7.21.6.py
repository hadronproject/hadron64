metadata = """
summary @ An URL retrival utility and library
homepage @ http://curl.haxx.se/
license @ MIT
src_url @ http://curl.haxx.se/download/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib dev-libs/openssl 
          app-misc/ca-certificates
"""

def configure():
	conf(
	"--with-random=/dev/urandom \
        --prefix=/usr \
        --mandir=/usr/share/man \
        --disable-dependency-tracking \
        --enable-ipv6 \
        --disable-ldaps \
        --disable-ldap \
        --enable-manual \
        --enable-versioned-symbols \
        --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
        --without-libidn \
        --enable-threaded-resolver")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
