metadata = """
summary @ Non-DNS IP-to-country resolver C library & utils
homepage @ http://www.maxmind.com/app/c
license @ GPL
src_url @ http://www.maxmind.com/download/geoip/api/c/GeoIP-$version.tar.gz
arch @ ~x86
options @ ipv6 perl-geoipupdate
"""

opt_runtime = """
perl-geoipupdate @ dev-perl/PerlIO-gzip dev-perl/libwww-perl
"""

def prepare():
    sed("""-e "s:usr local share GeoIP:usr share GeoIP:" -e "s:usr local etc:etc:" -i apps/geoipupdate-pureperl.pl""")

def configure():
    autoreconf("-i")
    conf(
    "--sysconfdir=/etc/geoip",
    config_enable("static-libs", "static"))

def build():
    make("check")

def install():
    if opt("ipv6"):
        insfile("GeoIPv6.dat", "/usr/share/GeoIP/GeoIPv6.dat")
    insdoc("AUTHORS", "ChangeLog", "README", "TODO", "conf/GeoIP.conf.default")

    raw_install("DESTDIR=%s install" % install_dir)
