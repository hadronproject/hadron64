metadata = """
summary @ Download utility that supports HTTP(S), FTP, BitTorrent, and Metalink
homepage @ http://aria2.sourceforge.net/
license @ GPL
src_url @ http://downloads.sourceforge.net/aria2/$fullname.tar.bz2
arch @ ~x86
options @ ssl gnutls ares bittorrent sqlite scripts nls expat metalink xmlrpc
"""

depends = """
runtime @ sys-libs/glibc app-misc/ca-certificates 
"""

opt_runtime = """
ssl @
    gnutls @ net-libs/gnutls || dev-libs/openssl
ares @ net-dns/c-ares
bittorrent @
    gnutls @ dev-libs/libgcrypt net-libs/gnutls || dev-libs/openssl
metalink @
    expat @ dev-libs/expat || dev-libs/libxml2
sqlite @ dev-db/sqlite
xmlrpc @
    expat @ dev-libs/expat || dev-libs/libxml2
nls @ sys-devel/gettext
scripts @ dev-lang/ruby
"""

def configure():
    xmllib = ""
    if opt("metalink") or opt("xmlrpc"):
        if opt("expat"):
            xmllib += " --with-libexpat "
        if not opt("expat"):
            xmllib += " --with-libxml2 "

    conf(
    "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt",
    "--enable-epoll",
    "--enable-threads=posix",
    "--with-libz",
    config_enable("ares", "libcares"),
    config_enable("bittorrent"),
    config_enable("sqlite", "sqlite3"),
    config_enable("metalink"),
    config_enable("nls"), xmllib)

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("ChangeLog", "README", "AUTHORS", "NEWS")

