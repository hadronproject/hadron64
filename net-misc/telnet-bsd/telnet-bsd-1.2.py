metadata = """
summary @ Telnet and telnetd ported from OpenBSD with IPv6 support
homepage @ ftp://ftp.suse.com/pub/people/kukuk/ipv6/
license @ BSD
src_url @ ftp://ftp.suse.com/pub/people/kukuk/ipv6/$fullname.tar.bz2
arch @ ~x86_64
options @ xinetd
"""

depends = """
runtime @ sys-libs/ncurses
"""

opt_build = """
xinetd @ sys-apps/xinetd
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("README", "THANKS", "NEWS", "AUTHORS", "ChangeLog", "INSTALL")
    if opt("xinetd"):
        insexe("%s/telnet.xinetd" % filesdir, "/etc/xinetd.d/telnet")
