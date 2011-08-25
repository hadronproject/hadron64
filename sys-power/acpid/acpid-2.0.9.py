metadata = """
summary @ A daemon for delivering ACPI power management events with netlink support
homepage @ http://tedfelix.com/linux/acpid-netlink.html
license @ GPL
src_url @ http://www.tedfelix.com/linux/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ app-shells/bash
"""

def install():
    insexe("%s/acpid" % filesdir, "/etc/rc.d/acpid")
    insfile("%s/anything" % filesdir, "/etc/acpi/events/anything")
    insexe("%s/handler.sh" % filesdir, "/etc/acpi/handler.sh")
    insfile("%s/acpid.conf.d" % filesdir, "/etc/conf.d/acpid")

    raw_install("DESTDIR=%s" % install_dir)
