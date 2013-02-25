metadata = """
summary @ NTP (Network Time Protocol) tries to keep servers in sync
homepage @ http://www.ntp.org/
license @ as-is
src_url @ http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-4.2.6p4.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl sys-libs/readline sys-libs/libcap app-misc/iana-etc
build @ dev-perl/HTML-Parser
"""

srcdir = fullname+"p4"

def configure():
    system("rm -f aclocal.m4")
    system("libtoolize --copy --force")
    export("ac_cv_header_dns_sd_h", "0")
    export("LDFLAGS", "-Wl,--hash-style=gnu")
    conf("--enable-linux-caps")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insexe("%s/ntpd" % filesdir, "/etc/rc.d/ntpd")
    insexe("%s/ntpdate" % filesdir, "/etc/rc.d/ntpdate")
    insfile("%s/ntp.conf" % filesdir, "/etc/ntp.conf")
    insfile("%s/ntpd.conf" % filesdir, "/etc/conf.d/ntpd.conf")
	
    makedirs("/var/lib/ntp")
    system("rmdir %s/usr/{lib,sbin}" % install_dir)
