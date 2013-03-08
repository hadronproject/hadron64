metadata = """
summary @ ISC Dynamic Host Configuration Protocol (DHCP) client/server
homepage @ http://www.isc.org/products/DHCP
license @ ISC BSD SSLeay GPL-2
src_url @ ftp://ftp.isc.org/isc/$name/$version-P2/$fullname-P2.tar.gz
options @ ipv6 ldap server ssl
arch @ ~x86_64
"""

opt_common = """
ldap @ net-dns/openldap
ssl @ dev-libs/openssl
"""

depends = """
runtime @ sys-apps/iproute2 sys-apps/net-tools
"""

srcdir = "dhcp-4.2.4-P2"

def prepare():
    if not opt("server"):
        sed("-i -r -e '/^SUBDIRS/s:\<(dhcpctl|relay|server)\>::g' Makefile.in")

    sed("-i '/^CFLAGS=\"$CFLAGS/ s/INGS\"/INGS -D_GNU_SOURCE\"/' configure")

    if opt("ipv6"):
        patch("dhcp-4.1.1-missing-ipv6-not-fatal.patch")

def configure():
    myconf = "--with-cli-lease-file=/var/lib/dhclient/dhclient.leases"
    if opt("ipv6"):
        myconf += " --with-cli6-lease-file=/var/lib/dhclient/dhclient6.leases"
    if opt("server"):
        myconf += " --with-srv-lease-file=/var/lib/dhcp/dhcpd.leases"
        if opt("ipv6"):
            myconf += " --with-srv6-lease-file=/var/lib/dhcp/dhcpd6.leases"

    conf(config_with("ldap"),
        config_enable("ipv6", "dhcpv6"),
        "--enable-paranoia",
        "--enable-early-chroot",
        myconf)

def install():
    raw_install("DESTDIR=%s install" % install_dir)

    if opt("server"):
            insfile(joinpath(filesdir, "dhcpd4.service"),
                    "/usr/lib/systemd/system/dhcpd4.service")
            insfile(joinpath(filesdir, "dhcpd6.service"),
                    "/usr/lib/systemd/system/dhcpd6.service")
            insfile(joinpath(filesdir, "dhcp"), "/etc/conf.d/dhcp")

    insinto("client/scripts/linux", "/sbin/dhclient-script")

    insdoc("README", "LICENSE")
