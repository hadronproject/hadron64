metadata ="""
summary @ Next-generation syslogd with advanced networking and filtering capabilities
homepage @ http://www.balabit.com/network-security/syslog-ng/
license @ GPL-2
src_url @ http://www.balabit.com/downloads/files/$name/sources/$version/source/$name_$version.tar.gz
options @ pcre ssl caps ipv6 tcpd static
arch @ ~x86
"""

depends = """
build @ dev-util/pkg-config sys-devel/flex sys-libs/glib dev-libs/eventlog
"""

opt_build = """
ssl @ dev-libs/openssl
tcpd @ >=sys-apps/tcp-wrappers-7.6
caps @ sys-libs/libcap
pcre @ dev-libs/pcre
"""

opt_runtime = """
ssl @ dev-libs/openssl
tcpd @ >=sys-apps/tcp-wrappers-7.6
caps @ sys-libs/libcap
pcre @ dev-libs/pcre
"""

def prepare():
    patch(level=1)

def configure():
    myconf = ""
    if opt("static"):
        myconf += "--enable-static-linking"
        if opt("pcre"):
            myconf += " --disable-pcre"
    else:
        myconf += "--enable-dynamic-linking"

    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc/syslog-ng",
            "--libexecdir=/usr/lib",
            "--localstatedir=/var/lib/syslog-ng",
            "--enable-tcp-wrapper",
            "--with-pidfile-dir=/var/run",
            "--disable-spoof-source",
            "--disable-dependency-tracking",
            config_enable("caps", "linux-caps"),
            config_enable("pcre"),
            config_enable("ssl"),
            config_enable("tcpd", "tcp-wrapper"),
            config_enable("ipv6"),
            myconf)

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insfile("%s/syslog-ng.conf" % filesdir, "/etc/syslog-ng/syslog-ng.conf")
    insfile("%s/syslog-ng.logrotate" % filesdir, "/etc/logrotate.d/syslog-ng")
    insexe("%s/syslog-ng.rc" % filesdir, "/etc/logrotate.d/syslog-ng")
    makedirs("/var/lib/syslog-ng")
