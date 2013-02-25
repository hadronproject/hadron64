metadata = """
summary @ Modular text mode IRC client with Perl scripting
homepage @ http://irssi.org/
license @ GPL
src_url @ http://irssi.org/files/$fullname.tar.bz2
arch @ ~x86_64
options @ ipv6 ssl
"""

depends = """
runtime @ sys-libs/glibc sys-libs/glib dev-libs/openssl dev-lang/perl
"""

opt_runtime = """
ssl @ dev-libs/openssl
"""

def configure():
    conf(
    "--with-proxy \
--sysconfdir=/etc \
--with-perl-lib=vendor",
config_enable("ipv6"),
config_enable("ssl"))


def install():
    raw_install("DESTDIR=%s" % install_dir)
