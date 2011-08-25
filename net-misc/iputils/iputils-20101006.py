metadata = """
summary @ IP Configuration Utilities (and Ping)
homepage @ http://www.linuxfoundation.org/en/Net:Iputils
license @ GPL
src_url @ http://www.skbuff.net/$name/$name-s$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc dev-libs/openssl
          sys-fs/sysfsutils
"""

srcdir = "%s-s%s" % (name, version)

#def prepare():
#    patch(level=1)

def install():
    for a in ('ping', 'ping6'):
        insexe("%s/%s" % (build_dir, a), target="/bin/%s" % a)

    for b in ("clockdiff", "arping", "rdisc", "tracepath",
            "tracepath6", "traceroute6"):
        insexe("%s/%s" % (build_dir, b), target="/sbin/%s" % b)
