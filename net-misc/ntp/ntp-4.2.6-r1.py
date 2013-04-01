metadata = """
summary @ NTP (Network Time Protocol) tries to keep servers in sync
homepage @ http://www.ntp.org/
license @ as-is
src_url @ http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-4.2.6p5.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl sys-libs/readline sys-libs/libcap app-misc/iana-etc
build @ dev-perl/HTML-Parser
"""

srcdir = '%s-%sp5' % (name, raw_version)

def configure():
    conf("--enable-linux-caps")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/ntpd.service" % filesdir, "/usr/lib/systemd/system/ntpd.service")
    insfile("%s/ntpdate.service" % filesdir, "/usr/lib/systemd/system/ntpdate.service")
    insfile("%s/ntp.conf" % filesdir, "/etc/ntp.conf")
    insfile("%s/ntpd.conf" % filesdir, "/etc/conf.d/ntpd.conf")

def post_install():
    system("/usr/sbin/groupadd -g 123 ntp 2> /dev/null")
    system("/usr/sbin/useradd -u 123 -g ntp -s /sbin/nologin -d /etc/ntp ntp 2> /dev/null")

def post_remove():
    system("/usr/sbin/userdel ntp 2> /dev/null")
    system("/usr/sbin/groupdel ntp 2> /dev/null")
