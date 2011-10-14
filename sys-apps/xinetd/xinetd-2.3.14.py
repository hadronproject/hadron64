metadata = """
summary @ A secure replacement for inetd
homepage @ http://www.xinetd.org/
license @ custom
src_url @ http://www.xinetd.org/xinetd-$version.tar.gz
arch @ ~x86
options @ perl
"""

opt_runtime = """
perl @ dev-lang/perl
"""

def prepare():
    patch()

def configure():
    conf(
    "--with-loadavg",
    "--without-libwrap")

def install():
    raw_install("prefix=%s/usr MANDIR=%s/usr/share/man" % (install_dir, install_dir))
    insdoc("AUDIT", "INSTALL", "README", "TODO", "CHANGELOG")
    insexe("%s/xinetd" % filesdir, "/etc/rc.d/xinetd")
    insfile("%s/xinetd.conf" % filesdir, "/etc/xinetd.conf")
    insfile("%s/servers" % filesdir, "/etc/xinetd.d/servers")
    insfile("%s/services" % filesdir, "/etc/xinetd.d/services")
