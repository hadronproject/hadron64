metadata = """
summary @ HTTP and WebDAV client library
homepage @ http://www.webdav.org/neon/
license @ GPL2
src_url @ http://www.webdav.org/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/expat app-misc/ca-certificates net-libs/gnutls
build @ dev-util/pkg-config
"""

def configure():
    conf("--with-expat",
            "--enable-shared",
            "--disable-static",
            "--with-ssl=openssl",
            "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt")

def install():
    raw_install("DESTDIR=%s" % install_dir)
