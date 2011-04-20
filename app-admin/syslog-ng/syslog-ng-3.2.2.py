metadata ="""
summary @ Next-generation syslogd with advanced networking and filtering capabilities
homepage @ http://www.balabit.com/network-security/syslog-ng/
license @ GPL-2
src_url @ http://www.balabit.com/downloads/files/$name/sources/$version/source/$name_$version.tar.gz
arch @ ~x86
"""

def prepare():
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc/syslog-ng",
            "--libexecdir=/usr/lib",
            "--localstatedir=/var/lib/syslog-ng",
            "--enable-tcp-wrapper",
            "--with-pidfile-dir=/var/run",
            "--disable-spoof-source")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    copy("%s/syslog-ng.conf", "/etc/syslog-ng/syslog-ng.conf")
