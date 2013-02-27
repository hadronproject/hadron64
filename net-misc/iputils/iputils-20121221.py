metadata = """
summary @ IP Configuration Utilities (and Ping)
homepage @ http://www.linuxfoundation.org/en/Net:Iputils
license @ GPL
src_url @ http://www.skbuff.net/$name/$name-s$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/openssl
          sys-fs/sysfsutils
"""

srcdir = "%s-s%s" % (name, version)

def build():
    make("USE_GNUTLS=no CCOPTOPT='%s'" % get_env("CFLAGS"))

def install():
    for item in ('ping', 'ping6'):
        insexe("%s/%s" % (build_dir, item), target="/bin/%s" % item)

    for item in ("clockdiff", "arping", "rarpd", "rdisc", "tracepath",
            "tracepath6", "traceroute6", "tftpd"):
        insexe("%s/%s" % (build_dir, item), target="/sbin/%s" % item)

    # To install man pages, we must install docbook* packages
    #makedirs("/usr/share/man/man8")
    #for item in ("arping", "clockdiff", "ping", "rarpd", \
    #        "rdisc", "tftpd", "tracepath"):
    #    insfile("doc/%s.8" % item, "/usr/share/man/man8/%s" % item)

