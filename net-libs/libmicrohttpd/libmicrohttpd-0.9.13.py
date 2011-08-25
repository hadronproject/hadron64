metadata ="""
summary @ A small C library that makes it easy to run an HTTP server as part of another application.
homepage @ http://www.gnu.org/s/libmicrohttpd/
license @ LGPL-2.1
src_url @ http://ftp.cc.uoc.gr/mirrors/gnu/$name/$name-$version.tar.gz
options @ ssl messages test
arch @ ~x86
"""

depends = """
build @ net-misc/curl
runtime @ net-misc/curl
"""

opt_build = """
ssl @ dev-libs/openssl net-libs/gnutls
"""

opt_runtime = """
ssl @ dev-libs/openssl dev-libs/libgcrypt net-libs/gnutls
"""

def configure():
    raw_configure("--prefix=/usr",
            "--enable-curl",
            config_enable("ssl", "https"),
            config_with("ssl", "gnutls"),
            config_enable("messages"),
            config_enable("test"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS","NEWS","README","ChangeLog")
