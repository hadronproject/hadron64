metadata = """
summary @ RFC2131 compliant DHCP client daemon
homepage @ http://roy.marples.name/dhcpcd/
license @ BSD
src_url @ http://roy.marples.name/downloads/$name/$fullname.tar.bz2
arch @ ~x86
"""

prepare = lambda: patch(level=1)

def configure():
    raw_configure("--libexecdir=/usr/lib/dhcpcd",
            "--dbdir=/var/lib/dhcpcd")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makesym("/sbin/dhcpcd", "/usr/bin/dhcpcd")

    insfile("%s/dhcpcd.conf.d" % filesdir, "/etc/conf.d/dhcpcd")

    echo("noipv4ll", "/etc/dhcpcd.conf")
